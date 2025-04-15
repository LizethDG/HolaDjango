from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # O tu modelo de usuario personalizado si lo tienes

# Puedes usar UserCreationForm directamente en la vista,
# o crear una clase personalizada aquí si necesitas añadir/modificar campos.
# Ejemplo de personalización (si quisieras añadir email, por ejemplo):
# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta(UserCreationForm.Meta):
#         model = User # O tu modelo personalizado
#         fields = UserCreationForm.Meta.fields + ('email',)

# Por ahora, no necesitamos un forms.py complejo, usaremos UserCreationForm en la vista.
# Este archivo puede quedar así o incluso vacío por el momento.