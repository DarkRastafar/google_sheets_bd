from django.db import models


class RangeModel(models.Model):
    range_field = models.CharField(max_length=120, verbose_name='Диапазон', null=True, blank=True)

    def __str__(self):
        return f'{self.range_field}'

    class Meta:
        verbose_name = 'Диапазон'
        verbose_name_plural = 'Диапазоны'


class Clients(models.Model):
    range_field = models.ForeignKey(RangeModel, verbose_name="Диапазон", on_delete=models.CASCADE, null=True,
                                    blank=True)
    inn = models.CharField(max_length=12, verbose_name='ИНН', unique=True)
    name_company = models.CharField(max_length=500, verbose_name='Компания', blank=True, default='')
    surname = models.CharField(max_length=120, verbose_name='Фамилия', blank=True, default='')
    first_name = models.CharField(max_length=120, verbose_name='Имя', blank=True, default='')
    patronomic = models.CharField(max_length=120, verbose_name='Отчество', blank=True, default='')
    phone = models.CharField(max_length=15, verbose_name='Телефон', blank=True, default='')
    adress = models.CharField(max_length=500, verbose_name='адрес', blank=True, default='')
    adress_one = models.CharField(max_length=120, blank=True, default='')
    adress_two = models.CharField(max_length=120, blank=True, default='')
    date = models.CharField(max_length=120, blank=True, default='')

    priority = models.CharField(max_length=10, verbose_name='Приоритет', blank=True, default='')
    check_priority = models.BooleanField('Проверить ИНН', default=True)
    make_general_comment = models.CharField(max_length=120, verbose_name='Сделать общий комментарий', blank=True)

    alfa_status_inn = models.CharField(max_length=120, verbose_name='Статус ИНН Альфа', blank=True, default='')
    alfa_comment = models.CharField(max_length=300, verbose_name='Коммент Альфа', blank=True, default='')
    alfa_add_comment = models.CharField(max_length=300, verbose_name='Доп. коммент Альфа', null=True, blank=True)
    alfa_str_comment = models.CharField(max_length=120, blank=True, default='')
    alfa_send = models.BooleanField('Отправить РКО Альфа', default=False)
    alfa_client_type = models.CharField(max_length=120, verbose_name='Тип клиента Альфа', blank=True, default='')
    alfa_city = models.CharField(max_length=120, verbose_name='город банка Альфа', blank=True, default='')
    alfa_response = models.TextField(verbose_name='Ответ банка Альфа', blank=True, default='')
    alfa_fias = models.CharField(max_length=120, verbose_name='Fias Альфа', blank=True, default='')
    alfa_ekvairing = models.CharField(max_length=120, blank=True, default='')
    alfa_spec_schet_44 = models.CharField(max_length=120, blank=True, default='')
    alfa_credit = models.CharField(max_length=120, blank=True, default='')

    vtb_status_inn = models.CharField(max_length=120, verbose_name='Статус ИНН ВТБ', blank=True, default='')
    vtb_comment = models.CharField(max_length=300, verbose_name='Коммент ВТБ', blank=True, default='')
    vtb_add_comment = models.CharField(max_length=300, verbose_name='Доп. коммент ВТБ', null=True, blank=True)
    vtb_to_fix = models.BooleanField('Закрепить ВТБ', default=False)
    vtb_send = models.BooleanField('Отправить ВТБ', default=False)
    vtb_client_type = models.CharField(max_length=120, verbose_name='Тип клиента ВТБ', blank=True, default='')
    vtb_city = models.CharField(max_length=120, verbose_name='Город банка ВТБ', blank=True, default='')
    vtb_response = models.TextField(verbose_name='Ответ банка ВТБ', blank=True, default='')
    vtb_application_ID = models.TextField(verbose_name='ID заявки ВТБ', blank=True, default='')

    tinkoff_status_inn = models.CharField(max_length=120, verbose_name='Статус ИНН Тинькофф', blank=True, default='')
    tinkoff_comment = models.CharField(max_length=300, verbose_name='Коммент Тинькофф', blank=True, default='')
    tinkoff_add_comment = models.CharField(max_length=300, verbose_name='Доп. коммент Тинькофф',
                                                  null=True, blank=True)
    tinkoff_send = models.BooleanField('Отправить Тинькофф', default=False)
    tinkoff_client_type = models.CharField(max_length=120, verbose_name='Тип клиента Тинькофф', blank=True, default='')
    tinkoff_city = models.CharField(max_length=120, verbose_name='Город банка Тинькофф', blank=True, default='')
    tinkoff_response = models.TextField(verbose_name='Ответ банка Тинькофф', blank=True, default='')

    otkritie_status_inn = models.CharField(max_length=120, verbose_name='Статус ИНН Открытие', blank=True, default='')
    otkritie_comment = models.CharField(max_length=300, verbose_name='Коммент Открытие', blank=True, default='')
    otkritie_add_comment = models.CharField(max_length=300, verbose_name='Доп. коммент Открытие',
                                                   null=True, blank=True)
    otkritie_send = models.BooleanField('Отправить Открытие', default=False)
    otkritie_client_type = models.CharField(max_length=120, verbose_name='Тип клиента Открытие', blank=True, default='')
    otkritie_city = models.CharField(max_length=120, verbose_name='Город банка Открытие', blank=True, default='')
    otkritie_response = models.TextField(verbose_name='Ответ банка Открытие', blank=True, default='')
    otkritie_ekvaring = models.BooleanField('Эквайринг Открытие', default=False)

    tochka_status_inn = models.CharField(max_length=120, verbose_name='Статус ИНН Точка', blank=True, default='')
    tochka_comment = models.CharField(max_length=300, verbose_name='Коммент Точка', blank=True, default='')
    tochka_add_comment = models.CharField(max_length=300, verbose_name='Доп. коммент Точка',
                                                 null=True, blank=True)
    tochka_send = models.BooleanField('Отправить Точка', default=False)
    tochka_client_type = models.CharField(max_length=120, verbose_name='Тип клиента Точка', blank=True, default='')
    tochka_city = models.CharField(max_length=120, verbose_name='Город банка Точка', blank=True, default='')
    tochka_dont_send = models.CharField(max_length=120, verbose_name='Не звонить Точка', blank=True, default='')
    tochka_checkbox = models.CharField(max_length=120, blank=True, default='')

    psb_status_inn = models.CharField(max_length=120, verbose_name='Статус ИНН ПСБ', blank=True, default='')
    psb_comment = models.CharField(max_length=300, verbose_name='Коммент ПСБ', blank=True, default='')
    psb_add_comment = models.CharField(max_length=300, verbose_name='Доп. коммент ПСБ', null=True, blank=True)
    psb_send = models.BooleanField('Отправить ПСБ', default=False)
    psb_client_type = models.CharField(max_length=120, verbose_name='Тип клиента ПСБ', blank=True, default='')
    psb_city = models.CharField(max_length=120, verbose_name='Город банка ПСБ', blank=True, default='')
    psb_response = models.TextField(verbose_name='Ответ банка ПСБ', blank=True, default='')
    psb_application_ID = models.TextField(verbose_name='ID заявки ПСБ', blank=True, default='')

    module_comment = models.CharField(max_length=300, verbose_name='Коммент Модуль', blank=True, default='')
    module_add_comment = models.CharField(max_length=300, verbose_name='Доп. коммент Модуль',
                                                 null=True, blank=True)
    module_send = models.BooleanField('Отправить Модуль', default=False)
    module_client_type = models.CharField(max_length=120, verbose_name='Тип клиента Модуль', blank=True, default='')
    module_city = models.CharField(max_length=120, verbose_name='Город банка Модуль', blank=True, default='')
    module_response = models.TextField(verbose_name='Ответ банка Модуль', blank=True, default='')
    module_application_ID = models.TextField(verbose_name='ID заявки Модуль', blank=True, default='')

    date_create_client = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.inn}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class SheetsResponses(models.Model):
    range_field = models.ForeignKey(RangeModel, verbose_name="Диапазон", on_delete=models.CASCADE, null=True, blank=True)
    response = models.TextField('Ответ из таблицы', null=True, blank=True)

    def __str__(self):
        return f'{self.range_field}'

    class Meta:
        verbose_name = 'Ответ таблицы'
        verbose_name_plural = 'Ответы таблиц'

