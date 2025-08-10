from django.db import models
from django.contrib.auth.models import User


class Clients(models.Model):
    '''Модель описывающая клиентов фирмы'''

    class Status(models.TextChoices):
        ACTIVE = 'AC', 'active'
        INACTIVE = 'INAC', 'inactive'
        POTENTIAL = 'PO', 'potential'

    # Общая информация о клиенте закинем их в форму
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    # Даты
    created_at = models.DateTimeField(auto_now_add=True)  # дата добавления в бд
    updated_at = models.DateTimeField(auto_now=True)  # дата обновления данных
    # Деньги
    total_spent = models.DecimalField(decimal_places=2, max_digits=20, default=0)  # сколько он денег потратил
    last_deal_price = models.DecimalField(decimal_places=2, max_digits=10, default=0) #  Цена последней сделки
    last_connection = models.DateTimeField(null=True, blank=True)  # когда в последний раз клиент что-то покупал
    # Остальное
    notes = models.TextField(blank=True, default='')  # какие-нибудь заметки
    status = models.CharField(choices=Status.choices, default=Status.POTENTIAL, null=False)  # Статус клиента
    # Связи
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                             related_name='clients')  # Связь между моделями User-->ClientsModel

    def str(self):
        return f'{self.first_name}, {self.last_name}, {self.last_connection}, {self.total_spent}'

    def get_full_name(self):
        '''Вернет полное имя клиента'''
        return f'{self.first_name}, {self.last_name}'

    #def total_price_counter(self):
    #    if self.last_deal_price:
    #        self.total_spent += self.last_deal_price
    #    else:
    #        pass


    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-created_at']