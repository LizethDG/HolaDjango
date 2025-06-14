from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Correo electrónico", max_length=254)

class EmailUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", max_length=30, required=True)
    email = forms.EmailField(label="Correo electrónico", max_length=254, required=True)

    class Meta:
        model = User
        fields = ("first_name", "email")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.username = self.cleaned_data["email"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user