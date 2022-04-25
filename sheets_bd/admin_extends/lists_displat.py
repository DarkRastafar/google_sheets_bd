from sheets_bd.functions.models_methods import return_model_fields


alfabank_list_display = return_model_fields('alfa')
vtb_list_display = return_model_fields('vtb')
tinkoff_list_display = return_model_fields('tinkoff')
otkritie_list_display = return_model_fields('otkritie')
tochka_list_display = return_model_fields('tochka')
psb_list_display = return_model_fields('psb')
module_list_display = return_model_fields('module')
main_list_display = return_model_fields()


full_list_display = main_list_display + alfabank_list_display + vtb_list_display + tinkoff_list_display + \
                    otkritie_list_display + tochka_list_display + psb_list_display + module_list_display + \
                    ['date_create_client']
