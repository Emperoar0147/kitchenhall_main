from .models import User, Staff, Customer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

"""def authenticate(username, password):
    return User.authenticateUser(username, password)"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'user_type']
        extra_kwargs = {"password": {"write_only": True},"user_type": {"read_only": True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'email', 'username', 'password', 'user_type']
        extra_kwargs = {"password": {"write_only": True},"user_type": {"write_only": True}}

        def create(self, validated_data):
            user = Staff.staff.create_user(**validated_data)
            return user


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'email', 'username', 'password', 'user_type']
        extra_kwargs = {"password": {"write_only": True}, "user_type": {"write_only": True}}

        def create(self, validated_data):
            user = Customer.customer.create_user(**validated_data)
            return user 

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid credentials')

        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
        return {'token': f'Bearer {token}'}

class ActivateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(style={'input': 'password'}, max_length=6)

    def validate(self, attrs):
        email = attrs.get("email")
        otp = attrs.get("otp")

        try:
            user = User.objects.get(email=email)
            valid_otp = user.verify_pin(otp)

            if valid_otp:
                user.is_activated = True

            return {'user': user }
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid credentials')



        