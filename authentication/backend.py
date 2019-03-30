
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()

class EmailBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
            """
            Overrides Django default authenticate method to enable Login with email
            :param request:
            :param username:
            :param password:
            :param kwargs:
            :return:
            """

            try:
                if username is None:
                    email = kwargs.get(UserModel.EMAIL_FIELD)
                    user = UserModel._default_manager.get_by_natural_key(email)
                elif username:
                    username = kwargs.get(UserModel.USERNAME_FIELD)
                    user = UserModel._default_manager.get_by_natural_key(username)
            except UserModel.DoesNotExist:
                # Run the default password hasher once to reduce the timing
                # difference between an existing and a nonexistent user (#20760).
                UserModel().set_password(password)
            else:
                if user.check_password(password) and self.user_can_authenticate(user):
                    return user
