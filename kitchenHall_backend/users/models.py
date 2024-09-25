from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser

# Create your models here.


"""
Custom managers for different account types 
"""

class CustomUserManager(BaseUserManager):
    pass


class CustomerManager(BaseUserManager):
    """
    Manager for user_account_type set to 'Customer'
    """

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(user_type=User.USER_ACCOUNT_TYPE[2][0])


class StaffManager(BaseUserManager):
    """
    Manager for user_account_type set to 'Staff'
    """

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(user_type=User.USER_ACCOUNT_TYPE[1][0])




"""
Different account types models definitions
"""
class User(AbstractUser, PermissionsMixin):
    """
    Default user model class definition that is being used for the Admin User Type
    """

    USER_ACCOUNT_TYPE = [
        ('ADMIN', 'admin'),
        ('STAFF', 'staff'),
        ('CUSTOMER', 'customer')
    ]

    base_role = USER_ACCOUNT_TYPE[0][0]
    
    user_type = models.CharField(
        max_length=10,
        choices=USER_ACCOUNT_TYPE
    )

    activation_pin = models.CharField(
        max_length=6,
        blank=True,
        null=True
    )
    email = models.EmailField(unique=True)
    is_activated = models.BooleanField(default=False)
    is_superuser = True
    is_staff = True
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']

    
    def save(self, *args, **kwargs):
        """
        method to save a user into the User table in the database
        """
        if not self.pk:
            self.user_type = self.base_role
            return super().save(*args, **kwargs)

    def generate_pin(self):
        """
        method to return 6 digit code
        """
        from random import randint

        pin = ''.join([str(randint(0,9)) for i in range(6)])
        return pin

    def verify_pin(self, otp):
        return self.activation_pin == otp

    def __str__(self):
        return f'{self.__dict__}'

class Staff(User):
    """
    user model class definition that is being used for the Staff User Type
    """

    base_role = User.USER_ACCOUNT_TYPE[1][0]
    staff = StaffManager()
    is_staff = True

    class Meta:
        proxy = True
    

class Customer(User):
    """
    user model class definition that is being used for the Customer User Type
    """

    base_role = User.USER_ACCOUNT_TYPE[2][0]
    customer = CustomerManager()

    class Meta:
        proxy = True
    is_staff = False
