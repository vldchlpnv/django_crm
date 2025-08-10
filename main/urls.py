from django.urls import path, include
from .views import MainPageView, ProfileView, HellowPageView

app_name = 'main'


urlpatterns = [path('main_page/', MainPageView.as_view(), name='main_page'),
               path('user_profile/', ProfileView.as_view(), name='user_profile'),
               path('hellow_page/', HellowPageView.as_view(), name='hellow_page')]