from django.shortcuts import render
from django.db import IntegrityError
from django.core.mail import send_mail
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken



# create a mixin class that dynamically handles the serializer to be used based on the user_type

class DynamicSerializerMixin:
    """
    Dynamically set the serializer to be used for different user_type
    """
    serializer_class = None
     
    def get_serializer_class(self):
        user_type = self.request.data.get('user_type')

        if  user_type == "Staff".upper():
            self.serializer_class = StaffSerializer
        elif user_type == "Customer".upper():
            self.serializer_class = CustomerSerializer
        else:
            self.serializer_class = UserSerializer
        return self.serializer_class

# Create your views here.

class UserRegistrationView(DynamicSerializerMixin, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']


        # Check if the user already exists
        if User.objects.filter(email=email).exists():
            return Response({'error': 'User with this email already exists'}, status=status.HTTP_409_CONFLICT)

        # Create the new user
        user = serializer.save()

        # generate otp to be used to activate user
        activation_pin = user.generate_pin()

        # set generated otp for user
        user.activation_pin = activation_pin
        print(user.__dict__)
        
        # Send the OTP via email
        send_mail( 
            'OTP Verification',
            f'Your Activation PIN is {activation_pin}',
            'youremail@example.com',
            [user.email],
            fail_silently=False,
        )
        
        return Response({"message": "User registered successfully. OTP sent to your email"}, status=status.HTTP_201_CREATED)

class GetAllUsersView(DynamicSerializerMixin, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.validated_data['token']
        return Response({'token': token}, status=status.HTTP_200_OK)

class ActivateUserView(DynamicSerializerMixin, APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ActivateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        user.is_activated = True
        user.save()
        return Response({'response': 'User is activated'}, status=status.HTTP_200_OK)

class UserDetailView(DynamicSerializerMixin, generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileManagementView(DynamicSerializerMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password')

        user = None
        try:
            user = validate_email(email)
            is_email = True
        except ValidationError:
            is_email = False

        if is_email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, 'Email is not yet registered')
                return redirect('loginpage')
        else:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                messages.error(request, 'No account found with this is username')
                return redirect('loginpage')

        if user:
            authenticated_user = authenticate(request,  username=user.username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('dashboad_page', authenticated_user)
            else:
                messages.error(request, 'Invalid password, please try again')
                return redirect('loginpage')
    return render(request, 'login.html')


def verify_account_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = request.POST.get('otp')

        user = None

        try:
            user = User.objects.filter(email=email)

        except User.DoesNotExist:
            messages.error(request, 'This user does not exist')

        if user.activation_pin != otp:
            messages.error(request, 'invalid otp...please check the otp and retry again')
            return redirect('verifyaccount_page')

        user.is_activated = True
        return redirect('dashboard_page')
        
    return render(request, 'verifyaccount.html')

def dashboard_view(request, pk):
    pass

def logout_view(request):
    logout(request)
    return redirect('login_page')

def profile_view(request, pk):
    user = 'retrieved user using pk'
    return redirect(request, 'profile.html', {'current_user': user})
    pass

def updatepassword_view(request, pk):
    return render(request, 'updatepassword.html')
    pass

def changepassword_view(request):
    pass

# def manageitems_view(request, pk):
#     pass

# def view_listeditems_view(request, pk):
#     pass

# def current_user(self):
#    pass