from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


#LoginRequiredMixin  для запрета доступа не авторизованым пользователям пока нет пользовательской системы

class MainPageView(TemplateView):
    template_name = 'main/main_page.html'


class ProfileView(TemplateView):
    template_name = 'accounts/user_profile.html'

class HellowPageView(TemplateView):
    '''Страница на которую попадает пользователь без аутентификации'''
    template_name = 'main/hellow_page.html'