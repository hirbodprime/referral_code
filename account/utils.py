import random
import string

def generate_referral_code():
    length = 6
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_user_unique_code():
    length = 8
    characters = string.ascii_letters + string.digits
    char = ''.join(random.choice(characters) for _ in range(length))
    return f'SL{char}'
    


from django.shortcuts import redirect
from functools import wraps

def prevent_logged_in_access(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')  # Redirect to the dashboard or another page
        return view_func(request, *args, **kwargs)
    return _wrapped_view