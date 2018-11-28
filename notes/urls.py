from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('' , wbz , name = 'home'),
    path('wbz_bm' , wbz_bm , name = 'wbz_bm'),
    path('ybz/' , report_time_list , name = 'ybz'),
    path('ybz_detail/<int:rtl_id>' , ybz_detail , name = 'ybz_detail'),
    path('print_page/<int:user_id>/', print_page , name = 'print_page'),
#    path('login',LoginView.as_view(template_name='login.html'),name='login'),
    path('login', login ,name='login'),
    path('logout_view' , logout_view , name = 'logout_view'),
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
    path('report/<int:user_id>' , report , name = 'report'),
    path('report_bz/<int:user_id>' , report_bz , name = 'report_bz'),
    path('new_report_time/<int:user_id>' , new_report_time , name = 'new_report_time'),
    path('report_customer/<int:user_id>' , report_customer , name = 'report_customer'),
    path('ybz_bm/' , ybz_bm , name = 'ybz_bm'),
    path('ajax_unit_types' , ajax_unit_types , name = 'ajax_unit_types'),
    path('ajax_unit_models' , ajax_unit_models , name = 'ajax_unit_models'),
    path('download/' , download , name = 'download'),
    path('edit_report_time/<int:report_time_id>' , edit_report_time , name = 'edit_report_time'),
    
]
