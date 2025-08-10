from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import RegistrationForm
from django.contrib.auth.models import User

from django.views import View
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeView, \
    PasswordChangeDoneView


class SignUpView(View):
    '''Представление для регистрации пользователя и редирект его на рабочую страницу'''

    template_name = 'accounts/registration_form.html'

    def get(self, request):
        '''Вернет форму для регистрации'''
        registration_form = RegistrationForm()
        context = {'registration_form': registration_form}
        return render(request, self.template_name, context)

    def post(self, request):
        '''Отправит данные формы регистрации на сервер'''
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('main:main_page')

        context = {'registration_form': registration_form}
        return render(request, self.template_name, context)


class Login(LoginView):
    '''Класс входа пользователя в аккаунт'''
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('main:main_page')


class Logout(LogoutView):
    '''Класс выхода из аккаунта'''
    template_name = 'registration/logged_out.html'
    next_page = reverse_lazy('main:hellow_page')


class ChangePassword(PasswordChangeView):
    '''Изменение пароля'''
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('accounts:password_change_done')
    title = 'Смена пароля'


class ChangeDone(PasswordChangeDoneView):
    '''Шаблон успешного зменения пароля и перехода на главную'''
    template_name = "registration/password_change_done.html"
    title = "Пароль успешно изменен!"
