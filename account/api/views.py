from rest_framework import generics, status, renderers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from account.models import UserProfile
from account.utils import generate_referral_code
from account.models import CustomUser
from .serializers import UserRegistrationSerializer,UserSerializer,UserProfileSerializer

class UserReferralCodeView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_profile = UserProfile.objects.get(user=self.request.user)
        return user_profile

    

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        if not UserProfile.objects.filter(user=user).exists():
            referral_code = generate_referral_code()
            UserProfile.objects.create(user=user, referral_code=referral_code)
        login(self.request, user)
    
    # Ensure JSON response only
    renderer_classes = (renderers.JSONRenderer,)


class UserLoginView(generics.CreateAPIView):
    serializer_class = AuthenticationForm

    def perform_create(self, serializer):
        login_form = serializer.validated_data
        user = login_form.get_user()
        login(self.request, user)
    
    # Ensure JSON response only
    renderer_classes = (renderers.JSONRenderer,)

class UserLogoutView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    
    # Ensure JSON response only
    renderer_classes = (renderers.JSONRenderer,)





class UserProfileList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserProfileDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
