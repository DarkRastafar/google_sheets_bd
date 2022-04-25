

clients_fieldsets = [(None, {
        'fields': (('inn', 'name_company', 'surname', 'first_name', 'patronomic',),
                   ('phone', 'adress', 'adress_one', 'adress_two', 'date',),
                   ('priority', 'check_priority', 'make_general_comment',),)
    }),
                 ('Альфабанк', {
                     'fields': (('alfa_status_inn', 'alfa_comment', 'alfa_add_comment'),
                                ('alfa_str_comment', 'alfa_client_type', 'alfa_city', ),
                                ('alfa_response', 'alfa_fias', 'alfa_ekvairing', ),
                                ('alfa_spec_schet_44', 'alfa_credit', 'alfa_send',),)
                 }),
                 ('ВТБ', {
                     'fields': (('vtb_status_inn', 'vtb_comment', 'vtb_add_comment',),
                                ('vtb_client_type', 'vtb_response', 'vtb_application_ID'),
                                ('vtb_city', 'vtb_to_fix', 'vtb_send',),)
                 }),
                 ('Тинькофф', {
                     'fields': (('tinkoff_status_inn', 'tinkoff_comment', 'tinkoff_add_comment'),
                                ('tinkoff_client_type', 'tinkoff_city', 'tinkoff_response'),
                                ('tinkoff_send',),)
                 }),
                 ('Открытие', {
                     'fields': (('otkritie_status_inn', 'otkritie_comment', 'otkritie_add_comment'),
                                ('otkritie_client_type', 'otkritie_city', 'otkritie_response'),
                                ('otkritie_send', 'otkritie_ekvaring'),)
                 }),
                 ('Точка', {
                     'fields': (('tochka_status_inn', 'tochka_comment', 'tochka_add_comment'),
                                ('tochka_client_type', 'tochka_city', 'tochka_dont_send'),
                                ('tochka_send',),)
                 }),
                 ('ПСБ', {
                     'fields': (('psb_status_inn', 'psb_comment', 'psb_add_comment'),
                                ('psb_client_type', 'psb_city', 'psb_response', 'psb_application_ID'),
                                ('psb_send',),)
                 }),
                 ('Модуль', {
                     'fields': (('module_comment', 'module_add_comment', 'module_client_type'),
                                ('module_city', 'module_response', 'module_application_ID'),
                                ('module_send',),)
                 }),
                 ]