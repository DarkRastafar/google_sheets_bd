

clients_fieldsets = [(None, {
        'fields': (('inn', 'name_company', 'surname', 'first_name', 'patronomic',),
                   ('phone', 'adress', 'adress_one', 'adress_two', 'date',),
                   ('priority', 'check_priority', 'make_general_comment',),)
    }),
                 ('Альфабанк', {
                     'fields': (('alfa_status_inn', 'alfa_comment', 'alfa_additional_comment'),
                                ('alfa_str_comment', 'alfa_client_type', 'alfa_bank_city', ),
                                ('alfa_bank_response', 'alfa_fias', 'alfa_ekvairing', ),
                                ('alfa_spec_schet_44', 'alfa_credit', 'alfa_send_rko',),)
                 }),
                 ('ВТБ', {
                     'fields': (('vtb_status_inn', 'vtb_comment', 'vtb_additional_comment',),
                                ('vtb_client_type', 'vtb_bank_response', 'vtb_id_application'),
                                ('vtb_bank_city', 'vtb_fixed', 'vtb_send',),)
                 }),
                 ('Тинькофф', {
                     'fields': (('tinkoff_status_inn', 'tinkoff_comment', 'tinkoff_additional_comment'),
                                ('tinkoff_client_type', 'tinkoff_bank_city', 'tinkoff_bank_response'),
                                ('tinkoff_send',),)
                 }),
                 ('Открытие', {
                     'fields': (('otkritie_status_inn', 'otkritie_comment', 'otkritie_additional_comment'),
                                ('otkritie_client_type', 'otkritie_bank_city', 'otkritie_bank_response'),
                                ('otkritie_send', 'otkritie_ekvaring'),)
                 }),
                 ('Точка', {
                     'fields': (('tochka_status_inn', 'tochka_comment', 'tochka_additional_comment'),
                                ('tochka_client_type', 'tochka_bank_city', 'tochka_do_not_call'),
                                ('tochka_send',),)
                 }),
                 ('ПСБ', {
                     'fields': (('psb_status_inn', 'psb_comment', 'psb_additional_comment'),
                                ('psb_client_type', 'psb_bank_city', 'psb_bank_response', 'psb_id_application'),
                                ('psb_send',),)
                 }),
                 ('Модуль', {
                     'fields': (('module_comment', 'module_additional_comment', 'module_client_type'),
                                ('module_bank_city', 'module_bank_response', 'module_id_application'),
                                ('module_send',),)
                 }),
                 ]