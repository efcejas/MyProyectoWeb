from django.test import TestCase
from django.contrib.auth import get_user_model
from residentesdm.backends import EmailBackend

class EmailBackendTest(TestCase):
    def setUp(self):
        self.backend = EmailBackend()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_authenticate_with_correct_credentials(self):
        user = self.backend.authenticate(None, 'test@example.com', 'testpassword')
        self.assertEqual(user, self.user)

    def test_authenticate_with_incorrect_password(self):
        user = self.backend.authenticate(None, 'test@example.com', 'wrongpassword')
        self.assertIsNone(user)

    def test_authenticate_with_nonexistent_email(self):
        user = self.backend.authenticate(None, 'nonexistent@example.com', 'testpassword')
        self.assertIsNone(user)
