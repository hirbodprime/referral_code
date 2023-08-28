import random
import string

def generate_referral_code():
    length = 6
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_user_unique_code():
    length = 6
    characters = string.digits
    char = ''.join(random.choice(characters) for _ in range(length))
    return f'FL{char}'
    

