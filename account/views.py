from django.shortcuts import render, redirect,get_object_or_404

from django.contrib import messages
from django.contrib.auth import login , logout,authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import  Permission
from django.db import transaction

from .forms import CustomUserCreationForm, CustomAuthenticationForm,CustomUserWithRefLinkCreationForm
from .models import UserProfile, CustomUser
from .utils import generate_referral_code



from django.contrib.auth import get_user_model
User = get_user_model()


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
            DS_NT = registration_form.cleaned_data['DS_NT']
            user.phone_number = phone_number
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            if referred_by_profile:
                user_profile, created = UserProfile.objects.get_or_create(user=user)
                user_profile.referrer = referred_by_profile.user
                user_profile.referral_level = referred_by_profile.referral_level + 1
                user_profile.DS_NT = DS_NT
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




def register_user(request):
    if request.user.is_authenticated:  
        return redirect('dashboard')
    
    if request.method == 'POST':
        registration_form = CustomUserCreationForm(request.POST)

        if registration_form.is_valid():
            user = registration_form.save()
            username = registration_form.cleaned_data['username']
            phone_number = registration_form.cleaned_data['phone_number']
            first_name = registration_form.cleaned_data['first_name']
            last_name = registration_form.cleaned_data['last_name']
            # referral_code = registration_form.cleaned_data['referral_code']  # Retrieve referral code
            
            user.phone_number = phone_number
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            
            # with transaction.atomic():
            #     if referral_code:
            #         try:
            #             referred_by_profile = UserProfile.objects.get(referral_code=referral_code)
                        
            #             # Update the referred user's UserProfile
            #             user_profile = UserProfile.objects.get(user=user)
            #             user_profile.referrer = referred_by_profile.user
            #             user_profile.save()
                        
            #             # Update the referrer's UserProfile
            #             referred_by_profile.used_referral_count += 1
            #             referred_by_profile.save()

            #             # Update referral levels
            #             user_level = referred_by_profile.referral_level + 1
            #             user_profile.referral_level = user_level
            #             user_profile.save()
            #         except UserProfile.DoesNotExist:
            #             pass  # Handle invalid referral code
                
            login(request, user)
            return redirect('dashboard')
        else:
            print("Form Errors:", registration_form.errors)
            print("Non-Field Errors:", registration_form.non_field_errors())
    else:
        registration_form = CustomUserCreationForm()
    
    return render(request, 'account/register.html', {'registration_form': registration_form})




def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        email = request.POST.get('email')  # Get the email from POST data
        password = request.POST.get('password')  # Get the password from POST data
        login_form = CustomAuthenticationForm(data={'username': email, 'password': password})
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            print("Form Errors:", login_form.errors)
            print("Non-Field Errors:", login_form.non_field_errors())
    else:
        login_form = CustomAuthenticationForm()
    
    return render(request, 'account/login.html', {'login_form': login_form})



@login_required
def profile_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        referral_code = user_profile.referral_code
        referred_users = UserProfile.objects.filter(referrer=request.user)
        user_unique_code = user_profile.user_unique_code
    except UserProfile.DoesNotExist:
        referral_code = None
        referred_users = []
        user_unique_code = None
    user_profile = UserProfile.objects.get(user=request.user)  # Get the user's profile
    return render(request, 'account/profile.html', {'u': user_profile , 'user_unique_code': user_unique_code, 'referral_code': referral_code, 'referred_users': referred_users})


def users_profile_view(req,username):
    user = get_object_or_404(User, username=username)
    user_profile = UserProfile.objects.get(user=user) 
    return render(req, 'account/profile.html',{'u':user_profile})
