from django.urls import path
from .views import ClientsInfoView, ClientsEditView

app_name = 'clients'

urlpatterns = [
    path('clients_list/', ClientsInfoView.as_view(), name='clients_list'),
    path('clients_edit/<int:id>/', ClientsEditView.as_view(), name='clients_edit')
]
