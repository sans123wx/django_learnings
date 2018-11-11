from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('' , wbz , name = 'home'),
    path('ybz/' , report_time_list , name = 'ybz'),
    path('ybz_detail/<int:rtl_id>' , ybz_detail , name = 'ybz_detail'),
    path('print_page/<int:cust>/', print_page , name = 'print_page'),
    path('login',LoginView.as_view(template_name='login.html'),name='login'),
    path('user_admin/<int:user_id>',user_admin , name = 'user_admin'),
    path('user_admin/ybz/<int:user_id>' , user_admin_ybz , name = 'user_admin_ybz'),
    path('management/<int:user_id>' , management , name = 'management'),
    path('management/customers/<int:user_id>' , management_customers , name = 'management_customers'),
    path('management/unit_types/<int:user_id>' , management_unit_types , name = 'management_unit_types'),
    path('management/unit_models/<int:user_id>' , management_unit_models , name = 'management_unit_models'),    
    path('new_note/<int:user_id>' , new_note , name = 'new_note'),
    path('new_customer/<int:user_id>' , new_customer , name = 'new_customer'),
    path('edit_customer/<int:customer_id>' , edit_customer , name = 'edit_customer'),
    path('new_unit_type/<int:user_id>' , new_unit_type , name = 'new_unit_type'),
    path('edit_unit_type/<int:unit_type_id>' , edit_unit_type , name = 'edit_unit_type'),
    path('new_unit_model/<int:user_id>' , new_unit_model , name = 'new_unit_model'),
    path('edit_unit_model/<int:unit_model_id>' , edit_unit_model , name = 'edit_unit_model'),
    path('edit_note/<int:note_id>' , edit_note , name = 'edit_note'),
    path('delete_note/<int:note_id> ', delete_note  , name = 'delete_note'),
    
    
]
