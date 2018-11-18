from django import forms
from .models import *
    
class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['date','售后','类别','型号','故障描述','价格','数量','教室','方式','通知时间','到校时间','返校时间']

class CustomerForm(forms.ModelForm):
    form_title = '售后单位'
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerForm_dj(CustomerForm):
    group = forms.ModelChoiceField(queryset = Group.objects.filter(id = 1))

class CustomerForm_wl(CustomerForm):
    group = forms.ModelChoiceField(queryset = Group.objects.filter(id = 2))

class Unit_typeForm(forms.ModelForm):
    form_title = '类别'
    class Meta:
        model = Unit_types
        fields = '__all__'

class Unit_typeForm_dj(Unit_typeForm):
    customer = forms.ModelChoiceField(queryset = Customer.objects.filter(group__id = 1))
    
class Unit_typeForm_wl(Unit_typeForm):
    customer = forms.ModelChoiceField(queryset = Customer.objects.filter(group__id = 2))

class Unit_modelForm(forms.ModelForm):
    form_title = '设备型号'
    class Meta:
        model = Unit_models
        fields = '__all__'

class Unit_modelForm_dj(Unit_modelForm):
    设备类型 = forms.ModelChoiceField(queryset = Unit_types.objects.filter(customer__group__id = 1))

class Unit_modelForm_wl(Unit_modelForm):
    设备类型 = forms.ModelChoiceField(queryset = Unit_types.objects.filter(customer__group__id = 2))
        
class Report_timeForm(forms.ModelForm):
    class Meta:
        model = Report_time
        fields = '__all__'
