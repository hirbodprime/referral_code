from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



DS_NT_choices = (
    ('Networker','Networker'),
    ('Direct-Seller','Direct-Seller'),
    )

class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)  # Use set_password to hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, phone_number, first_name, last_name, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)  # Add username field
    phone_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    DS_NT = models.CharField(choices=DS_NT_choices,max_length=15,verbose_name='Direct or Networker', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number', 'first_name', 'last_name','DS_NT']  # Add username to REQUIRED_FIELDS
    # Other methods and __str__ definition
    def __str__(self):
        return self.email
    
from django.contrib.auth import get_user_model
User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_unique_code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    referral_code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    referrer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='referred_users')
    used_referral_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    referral_level = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.user}'

    
    
    def get_referral_link(self):
        return reverse('register_with_referral', kwargs={'referral_code': self.referral_code})
