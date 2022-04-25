

clients_fieldsets = [(None, {
        'fields': (('inn', 'name_company', 'surname', 'first_name', 'patronomic',),
                   ('phone', 'adress', 'adress_one', 'adress_two', 'date',),
                   ('priority', 'check_priority', 'make_general_comment',),)
    }),
                 ('Альфабанк', {
                     'fields': (('alfabank_status_inn', 'alfabank_comment', 'alfabank_add_comment'),
                                ('alfabank_str_comment', 'alfabank_client_type', 'alfabank_city', ),
                                ('alfabank_response', 'alfabank_fias', 'alfabank_ekvairing', ),
                                ('alfabank_spec_schet_44', 'alfabank_credit', 'alfabank_send',),)
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
                     'fields': (('open_status_inn', 'open_comment', 'open_add_comment'),
                                ('open_client_type', 'open_city', 'open_response'),
                                ('open_send', 'open_ekvairing'),)
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