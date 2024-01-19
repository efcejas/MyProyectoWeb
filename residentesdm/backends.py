from django.contrib.auth import get_user_model # Para obtener el modelo de usuario
from django.contrib.auth.backends import ModelBackend # Para crear un backend de autenticación

# Acá debo crear el backend de autenticación

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model() # Obtener el modelo de usuario
        try:
            user = UserModel.objects.get(email=username) # Obtener el usuario con el email
        except UserModel.DoesNotExist:
            return None # Si no existe, retornar None
        else:
            if user.check_password(password): # Si existe, verificar la contraseña
                return user # Si es correcta, retornar el usuario
        return None # Si no, retornar None