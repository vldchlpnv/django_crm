from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from .forms import ClientsForm
from .models import Clients


##################################################################################################################
# login_url = '/accounts/login/'  вот такая штука есть после создания приложения с авторизацией надо будет добавить LoginRequiredMixin
###################################################################################################################
#############
# Добавить пагинацию по 10 клиентов на странице
#########
class ClientsInfoView(View):
    template_name = 'clients_templates/clients_view_template.html'  # атрибут класса с указанием шаблона который будет использоваться

    def get(self, request):
        '''Вернем писок общий'''

        clients_list = Clients.objects.all().order_by('-id')  # что бы список строился по посленему добавленному сверху
        form = ClientsForm()
        context = {'clients_list': clients_list, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        '''Добавляем, удаляем, изменияем'''

        client_id = request.POST.get('id')
        action = request.POST.get('action')

        if action == 'create':  # На простом уровне рабочее
            form = ClientsForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, messages.SUCCESS, 'Клиент добавлен')
                return redirect('clients:clients_list')
            else:
                clients_list = Clients.objects.all().order_by('-id')
                context = {'clients_list': clients_list, 'form': form}
                messages.error(request, messages.ERROR, 'Форма не прошла валидацию, введите данные повторно')
                return render(request, self.template_name, context)

        elif action == 'delete':  # На простом уровне рабочее
            client_delete = get_object_or_404(Clients, id=client_id)
            client_delete.delete()
            messages.success(request, messages.SUCCESS, 'Данные удалены')
            return redirect('clients:clients_list')


class ClientsEditView(View):
    '''Изменяем данные клиента'''

    edit_template = 'clients_templates/edit_template.html'

    def get(self, request, id):
        '''Переходим на страничку с формой пустой'''

        clients = get_object_or_404(Clients, id=id)
        form = ClientsForm(instance=clients)
        context = {'form': form, 'clients': clients}
        return render(request, self.edit_template, context)

    def post(self, request, id):
        '''Форма для изменения данных'''

        clients = get_object_or_404(Clients, id=id)
        form = ClientsForm(request.POST, instance=clients)
        if form.is_valid():
            messages.success(request, messages.SUCCESS, 'Данные обновлены')
            form.save()
            return redirect('clients:clients_list')

        return render(request, self.edit_template, {'form': form, 'clients': clients})
