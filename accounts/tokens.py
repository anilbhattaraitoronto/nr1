from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class RegistrationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return(
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
        )
registration_activation_token = RegistrationTokenGenerator
