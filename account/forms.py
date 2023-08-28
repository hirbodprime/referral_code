from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import DS_NT_choices
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
    )
    phone_number = forms.CharField(
        max_length=15,
    )
    first_name = forms.CharField(
        max_length=30,
    )
    last_name = forms.CharField(
        max_length=30,
    )
    referral_code = forms.CharField(
        max_length=10,
        required=False,
    )
    
    DS_NT = forms.ChoiceField(
        choices=DS_NT_choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
    )
    class Meta:
        model = CustomUser
        fields = ['email','username', 'phone_number', 'first_name', 'last_name', 'password1', 'password2', 'referral_code','DS_NT']


class CustomUserWithRefLinkCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    DS_NT = forms.ChoiceField(
        choices=DS_NT_choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
    )
    class Meta:
        model = CustomUser
        fields = ['email','username', 'phone_number', 'first_name', 'last_name', 'password1', 'password2','DS_NT']

    def __init__(self, *args, **kwargs):
        referral_code = kwargs.pop('referral_code', None)
        super().__init__(*args, **kwargs)
        if referral_code:
            self.fields['referral_code'] = forms.CharField(initial=referral_code, widget=forms.HiddenInput)


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False

    def authenticate(self, request):
        # Get the entered email and password
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email is None or password is None:
            return

        # Authenticate the user using email and password
        user = authenticate(request, email=email, password=password)
        return user



