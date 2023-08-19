from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    referral_code = forms.CharField(max_length=10, required=False)  # Add this line
    
    class Meta:
        model = CustomUser
        fields = ['email', 'phone_number', 'first_name', 'last_name', 'password1', 'password2', 'referral_code']  # Include referral_code in fields

class CustomUserWithRefLinkCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'phone_number', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        referral_code = kwargs.pop('referral_code', None)
        super().__init__(*args, **kwargs)
        if referral_code:
            self.fields['referral_code'] = forms.CharField(initial=referral_code, widget=forms.HiddenInput)

class CustomAuthenticationForm(AuthenticationForm):
    pass  # You can customize this form further if needed




