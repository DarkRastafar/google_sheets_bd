main_list_display = ['inn', 'name_company', 'surname', 'first_name', 'patronomic',
                     'phone', 'adress', 'adress_one', 'adress_two', 'date', 'priority',
                     'check_priority', 'make_general_comment']

alfabank_list_display = ['alfa_status_inn', 'alfa_comment', 'alfa_additional_comment', 'alfa_str_comment',
                         'alfa_send_rko', 'alfa_client_type', 'alfa_bank_city', 'alfa_bank_response',
                         'alfa_fias', 'alfa_ekvairing', 'alfa_spec_schet_44', 'alfa_credit']

vtb_list_display = ['vtb_status_inn', 'vtb_comment', 'vtb_additional_comment', 'vtb_fixed',
                    'vtb_send', 'vtb_client_type', 'vtb_bank_city', 'vtb_bank_response', 'vtb_id_application']

tinkoff_list_display = ['tinkoff_status_inn', 'tinkoff_comment', 'tinkoff_additional_comment', 'tinkoff_send',
                        'tinkoff_client_type', 'tinkoff_bank_city', 'tinkoff_bank_response']

otkritie_list_display = ['otkritie_status_inn', 'otkritie_comment', 'otkritie_additional_comment',
                         'otkritie_send', 'otkritie_client_type', 'otkritie_bank_city', 'otkritie_bank_response',
                         'otkritie_ekvaring']

tochka_list_display = ['tochka_status_inn', 'tochka_comment', 'tochka_additional_comment', 'tochka_send',
                       'tochka_client_type', 'tochka_bank_city', 'tochka_do_not_call', 'tochka_checkbox']

psb_list_display = ['psb_status_inn', 'psb_comment', 'psb_additional_comment', 'psb_send', 'psb_client_type',
                    'psb_bank_city', 'psb_bank_response', 'psb_id_application']

module_list_display = ['module_comment', 'module_additional_comment', 'module_send', 'module_client_type',
                       'module_bank_city', 'module_bank_response', 'module_id_application']

full_list_display = main_list_display + alfabank_list_display + vtb_list_display + tinkoff_list_display + \
                    otkritie_list_display + tochka_list_display + psb_list_display + module_list_display + \
                    ['date_create_client']
