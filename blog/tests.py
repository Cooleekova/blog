from django.test import TestCase
from django.contrib.auth.password_validation import validate_password
from django.conf import settings
import os


class ConfigTest(TestCase):
    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get('SECRET_KEY')
        # self.assertNotEqual(SECRET_KEY, 'abc123')
        try:
            validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'Weak secret key: {e.messages}'
            self.fail(msg)


