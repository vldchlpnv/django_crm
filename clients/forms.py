from django import forms

from .models import Clients


class ClientsForm(forms.ModelForm):
    '''Класс для добавление данных о нашем клиенте'''

    class Meta:
        model = Clients
        fields = ['first_name', 'last_name', 'email', 'phone', 'last_deal_price', 'status', 'notes']
       # widgets = {'status':} поле пока таким оставлю потом дбавлю аттрибуты


    #def save(self, commit=True):

    #    clients = super().save(commit=False) # создаем экземпляр класса Clients без добавления в базу
    #    clients.total_price_counter()
        
    #    if commit:
    #        clients.save()
    #    return clients


