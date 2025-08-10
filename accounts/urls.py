from django.urls import path
from .views import SignUpView, Logout, Login, ChangePassword, ChangeDone
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('password_change/', ChangePassword.as_view(), name="password_change"),
    path('password_change/done', ChangeDone.as_view(), name="password_change_done")

]
