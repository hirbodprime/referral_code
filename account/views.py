from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login , logout,authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import  Permission

from .forms import CustomUserCreationForm, CustomAuthenticationForm,CustomUserWithRefLinkCreationForm
from .models import UserProfile
from .utils import generate_referral_code

from wallet.models import Wallet

from django.contrib.auth import get_user_model
User = get_user_model()
# ... other imports ...

def register_with_referral(request, referral_code):
    if request.user.is_authenticated:  
        return redirect('dashboard')

    try:
        referred_by_profile = UserProfile.objects.get(referral_code=referral_code)
    except UserProfile.DoesNotExist:
        referred_by_profile = None

    registration_form_kwargs = {}
    if referred_by_profile:
        registration_form_kwargs['referral_code'] = referral_code

    if request.method == 'POST':
        registration_form = CustomUserWithRefLinkCreationForm(request.POST, **registration_form_kwargs)
        if registration_form.is_valid():
            user = registration_form.save()
            phone_number = registration_form.cleaned_data['phone_number']
            first_name = registration_form.cleaned_data['first_name']
            last_name = registration_form.cleaned_data['last_name']
            user.phone_number = phone_number
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            if referred_by_profile:
                user_profile, created = UserProfile.objects.get_or_create(user=user)
                user_profile.referrer = referred_by_profile.user
                user_profile.save()

                referred_by_profile.used_referral_count += 1
                referred_by_profile.save()

            login(request, user)
            return redirect('dashboard')
    else:
        registration_form = CustomUserWithRefLinkCreationForm(**registration_form_kwargs)

    return render(request, 'account/register.html', {'registration_form': registration_form})


def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


from .models import UserProfile

def register_user(request):
    if request.user.is_authenticated:  
        return redirect('dashboard')
    
    if request.method == 'POST':
        registration_form = CustomUserCreationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            phone_number = registration_form.cleaned_data['phone_number']
            first_name = registration_form.cleaned_data['first_name']
            last_name = registration_form.cleaned_data['last_name']
            referral_code = registration_form.cleaned_data['referral_code']  # Retrieve referral code
            
            user.phone_number = phone_number
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            
            if referral_code:
                try:
                    referred_by_profile = UserProfile.objects.get(referral_code=referral_code)
                    
                    # Update the referred user's UserProfile
                    user_profile = UserProfile.objects.get(user=user)
                    user_profile.referrer = referred_by_profile.user
                    user_profile.save()
                    
                    # Update the referrer's UserProfile
                    referred_by_profile.used_referral_count += 1
                    referred_by_profile.save()
                except UserProfile.DoesNotExist:
                    pass  # Handle invalid referral code
                
            login(request, user)
            return redirect('dashboard')
    else:
        registration_form = CustomUserCreationForm()
    
    return render(request, 'account/register.html', {'registration_form': registration_form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        login_form = CustomAuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        login_form = CustomAuthenticationForm()
    
    return render(request, 'account/login.html', {'login_form': login_form})




@login_required
def view_referral_code(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'account/referral_code.html', {'referral_code': user_profile.referral_code})

    

@login_required
def dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        referral_code = user_profile.referral_code
        referred_users = UserProfile.objects.filter(referrer=request.user)
        user_unique_code = user_profile.user_unique_code
    except UserProfile.DoesNotExist:
        referral_code = None
        referred_users = []
        user_unique_code = None

    return render(request, 'account/dashboard.html', {'user_unique_code': user_unique_code, 'referral_code': referral_code, 'referred_users': referred_users})





