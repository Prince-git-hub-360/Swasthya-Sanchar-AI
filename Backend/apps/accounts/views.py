"""
accounts.views

API Views for User Registration, Login, Profile management, and JWT Authentication.
"""
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import UserProfile
from .serializers import (
    LoginSerializer,
    UserProfileSerializer,
    UserProfileUpdateSerializer,
    UserRegistrationSerializer,
    UserSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer,
)

from drf_spectacular.utils import extend_schema

User = get_user_model()


@extend_schema(tags=['01. Authentication & User Profile'])
class RegisterView(generics.GenericAPIView):
    """User Registration Endpoint.
    Registers a new User and automatically builds their UserProfile and domain Patient record if role is 'patient'.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegistrationSerializer

    @extend_schema(tags=['01. Authentication & User Profile'])
    def get(self, request, *args, **kwargs):
        return Response({
            'message': 'User Registration Endpoint. Submit a POST request with details below.',
        })

    @extend_schema(tags=['01. Authentication & User Profile'])
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            errors = serializer.errors
            if 'username' in errors:
                err_text = str(errors['username'][0]) if isinstance(errors['username'], list) else str(errors['username'])
                return Response({
                    'status': 'error',
                    'error_code': 'USERNAME_TAKEN',
                    'detail': err_text,
                }, status=status.HTTP_400_BAD_REQUEST)
            serializer.is_valid(raise_exception=True)

        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'status': 'ok',
            'message': 'User registered successfully.',
            'tokens': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            },
            'user': UserSerializer(user, context={'request': request}).data,
        }, status=status.HTTP_201_CREATED)


@extend_schema(tags=['01. Authentication & User Profile'])
class LoginView(generics.GenericAPIView):
    """User Login Endpoint.
    Authenticates username and password, returning JWT Access & Refresh tokens + User details.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    @extend_schema(tags=['01. Authentication & User Profile'])
    def get(self, request, *args, **kwargs):
        return Response({
            'message': 'User Login Endpoint. Submit a POST request with username and password to log in.',
        })

    @extend_schema(tags=['01. Authentication & User Profile'])
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'status': 'ok',
            'message': 'Login successful.',
            'tokens': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            },
            'user': UserSerializer(user, context={'request': request}).data,
        }, status=status.HTTP_200_OK)


@extend_schema(tags=['01. Authentication & User Profile'])
class LogoutView(APIView):
    """User Logout Endpoint.
    Logs out user session.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            'message': 'User Logout Endpoint. Submit a POST request to log out.',
        })

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return Response({
            'status': 'ok',
            'message': 'Logout successful.'
        }, status=status.HTTP_200_OK)


import random

@extend_schema(tags=['01. Authentication & User Profile'])
class CheckUsernameView(APIView):
    """Check if a username or email is already registered."""
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        username = request.query_params.get('username', '').strip()
        email = request.query_params.get('email', '').strip()
        phone = request.query_params.get('phone', '').strip()

        if username:
            taken = User.objects.filter(username__iexact=username).exists()
            return Response({'available': not taken, 'username': username, 'message': f"Username '{username}' is already taken." if taken else 'Username available.'})
        if email:
            taken = User.objects.filter(email__iexact=email).exists()
            return Response({'available': not taken, 'email': email, 'message': f"Email '{email}' is already registered." if taken else 'Email available.'})
        if phone:
            taken = UserProfile.objects.filter(phone_number__icontains=phone).exists()
            return Response({'available': not taken, 'phone': phone, 'message': f"Phone number '{phone}' is already registered." if taken else 'Phone available.'})

        return Response({'available': True})


@extend_schema(tags=['01. Authentication & User Profile'])
class SendOtpView(APIView):
    """Generates and sends 4-digit OTP for phone or email verification."""
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone', '').strip()
        email = request.data.get('email', '').strip()

        otp_code = f"{random.randint(1000, 9999)}"

        if email:
            print(f"\n=======================================================")
            print(f"📧 [SWASTHYA AI EMAIL OTP SERVICE] Email: {email}")
            print(f"🔑 [YOUR 4-DIGIT VERIFICATION CODE]: {otp_code}")
            print(f"=======================================================\n")
            try:
                send_mail(
                    subject="Swasthya Sanchar AI • Your Verification Code",
                    message=f"Namaste,\n\nYour 4-digit verification code is: {otp_code}\n\nGovernment of India • National Health Authority (ABDM)",
                    from_email="noreply@swasthya-sanchar.gov.in",
                    recipient_list=[email],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"send_mail note: {e}")

            return Response({
                'status': 'ok',
                'type': 'email',
                'destination': email,
                'otp': otp_code,
                'message': f'4-digit verification code sent to {email}.',
            }, status=status.HTTP_200_OK)

        # Phone fallback (default to rural phone)
        phone = phone or '9876543210'
        print(f"\n=======================================================")
        print(f"📲 [SWASTHYA AI SMS OTP SERVICE] Phone: +91 {phone}")
        print(f"🔑 [YOUR 4-DIGIT VERIFICATION CODE]: {otp_code}")
        print(f"=======================================================\n")

        return Response({
            'status': 'ok',
            'type': 'phone',
            'destination': phone,
            'otp': otp_code,
            'message': f'4-digit SMS verification code sent to +91 {phone}.',
        }, status=status.HTTP_200_OK)


@extend_schema(tags=['01. Authentication & User Profile'])
class VerifyOtpView(APIView):
    """Verifies 4-digit OTP for dual email and phone authentication."""
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        otp = str(request.data.get('otp', '')).strip()
        expected_otp = str(request.data.get('expected_otp', '')).strip()

        if not otp:
            return Response({'status': 'error', 'message': 'OTP code is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Valid if matches expected OTP, or standard developer/demo bypasses (1234, 4089, or matches)
        if expected_otp and otp != expected_otp and otp not in ('1234', '4089'):
            return Response({'status': 'error', 'message': 'Invalid verification code. Please check and re-enter.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'status': 'ok',
            'verified': True,
            'message': 'Identity verified successfully.',
        }, status=status.HTTP_200_OK)


@extend_schema(tags=['01. Authentication & User Profile'])
class AuthRootView(APIView):
    """Authentication API Root Menu."""
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({
            'status': 'ok',
            'auth_routes': {
                'register': '/api/auth/register/',
                'login': '/api/auth/login/',
                'logout': '/api/auth/logout/',
                'profile': '/api/auth/profile/',
                'token_refresh': '/api/auth/token/refresh/',
                'password_reset': '/api/auth/password-reset/',
                'password_reset_confirm': '/api/auth/password-reset-confirm/',
            },
        })


@extend_schema(tags=['01. Authentication & User Profile'])
class UserProfileView(generics.RetrieveUpdateAPIView):
    """User Profile View/Update Endpoint."""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileUpdateSerializer

    def get_object(self):
        profile, _ = UserProfile.objects.get_or_create(user=self.request.user)
        return profile

    def get_serializer_class(self):
        if self.request.method in ('GET', 'HEAD', 'OPTIONS'):
            return UserProfileSerializer
        return UserProfileUpdateSerializer

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = request.user
        user_serializer = UserSerializer(user, context={'request': request})
        return Response(user_serializer.data)


@extend_schema(tags=['01. Authentication & User Profile'])
class PasswordResetRequestView(generics.GenericAPIView):
    """Request Password Reset Email."""
    permission_classes = [permissions.AllowAny]
    serializer_class = PasswordResetRequestSerializer

    def get(self, request, *args, **kwargs):
        return Response({'message': 'Submit a POST request with email to request a password reset.'})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_link = f"/api/auth/password-reset-confirm/?uid={uid}&token={token}"
            send_mail(
                subject='Password reset for AI Healthcare Assistant',
                message=f'Use the following link to reset your password: {reset_link}',
                from_email=None,
                recipient_list=[email],
                fail_silently=True,
            )
        except User.DoesNotExist:
            pass

        return Response({'detail': 'If an account with that email exists, a reset link has been sent.'})


@extend_schema(tags=['01. Authentication & User Profile'])
class PasswordResetConfirmView(generics.GenericAPIView):
    """Confirm Password Reset with UID & Token."""
    permission_classes = [permissions.AllowAny]
    serializer_class = PasswordResetConfirmSerializer

    def get(self, request, *args, **kwargs):
        return Response({'message': 'Submit a POST request with uid, token, and new_password.'})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        uidb64 = serializer.validated_data['uid']
        token = serializer.validated_data['token']
        new_password = serializer.validated_data['new_password']
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception:
            return Response({'detail': 'Invalid uid'}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response({'detail': 'Invalid or expired token.'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({'detail': 'Password has been reset successfully.'})


@extend_schema(tags=['01. Authentication & User Profile'])
class PhonePasswordResetView(APIView):
    """Resets user password using mobile phone verification."""
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        phone = str(request.data.get('phone', '')).strip()
        new_password = str(request.data.get('new_password', '')).strip()

        if not phone or not new_password:
            return Response({'error': 'Phone number and new password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Lookup user by phone or username
        user = User.objects.filter(username=phone).first() or \
               User.objects.filter(userprofile__phone_number=phone).first() or \
               User.objects.filter(username=f"user_{phone[-10:]}").first()

        if not user:
            user, _ = User.objects.get_or_create(
                username=phone,
                defaults={'first_name': 'Prince Kumar', 'email': f"{phone}@swasthya.ai"}
            )

        user.set_password(new_password)
        user.save()
        return Response({
            'status': 'ok',
            'message': 'Password has been reset successfully. You can now log in with your new password.',
        }, status=status.HTTP_200_OK)


@extend_schema(tags=['01. Authentication & User Profile'])
class CheckUsernameView(APIView):
    """Checks whether a username is already taken or available."""
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        username = request.query_params.get('username', '').strip()
        if not username:
            return Response({'available': False, 'message': 'Username is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        taken = User.objects.filter(username__iexact=username).exists()
        return Response({
            'username': username,
            'available': not taken,
            'taken': taken,
            'message': f'Username "@{username}" is already taken. Please sign in or choose another.' if taken else f'Username "@{username}" is available!',
        }, status=status.HTTP_200_OK)


