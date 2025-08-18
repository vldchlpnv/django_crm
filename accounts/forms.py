from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class RegistrationForm(UserCreationForm):
    '''Форма для ввода данных при регистрации'''

    first_name = forms.CharField(max_length=50, label='Введите имя', required=True)
    last_name = forms.CharField(max_length=50, label='Введите фамлию', required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def clean_email(self):
        '''Проверим на уникальность Email'''
        new_email = self.cleaned_data.get('email')      # вытаскиваем из формы значение email
        check = User.objects.filter(email=new_email).exists()    # Делаем проверку на наличие дубликата
        if new_email and check:
            raise ValidationError('Введенная вами почта уже используется!')
        return new_email


class UserAuthenticationForm(AuthenticationForm):
    '''Класс формы логина пользователя'''

    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}), max_length=150)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}), label='Введите пароль')
    remember_me = forms.BooleanField(required=False, label='Запомнить меня')






