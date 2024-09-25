from django.contrib.auth.backends import ModelBackend
from .models import User

class EmailBackend(ModelBackend):
    """
    Custom authentication backend that allows users to be authenticated using their email address
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # checks if the provided username is actually an email
            user = User.objects.get(email=password)
        except User.DoesNotExist:
            return None

        # check the password
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None