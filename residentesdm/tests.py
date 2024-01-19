from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from residentesdm.backends import EmailBackend

# importaciones de la aplicación
from .models import MyUsuario
from .forms import MyUsuarioForm

# Acá va teste del backend de autenticación

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

# Acá va el tests de registro

class RegistrationTests(TestCase):
    def test_registration_view(self):
        # Define los datos de prueba que enviarás al formulario de registro
        data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'email': 'testuser@example.com',
            'fecha_nacimiento': '2000-01-01',
        }

        # Realiza una solicitud POST a la vista de registro con los datos de prueba
        response = self.client.post(reverse('residentesdm:register'), data)

        # Verifica que la respuesta sea un redireccionamiento exitoso
        self.assertEqual(response.status_code, 302)

        # Verifica que el usuario se haya creado en la base de datos
        self.assertTrue(MyUsuario.objects.filter(username='testuser').exists())

        # Puedes agregar más aserciones según lo que desees probar en tu vista
        # Por ejemplo, verificar que el usuario esté correctamente autenticado después del registro
        user = MyUsuario.objects.get(username='testuser')
        self.assertTrue(user.is_authenticated)
