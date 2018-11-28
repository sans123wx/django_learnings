from django import forms
from .models import *
from django.contrib import auth
    
class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['date','售后','类别','型号','sn','故障描述','价格','数量','教室','方式','asp','telephone','通知时间','到校时间','返校时间','scraped']
        widgets = {
                'date':forms.DateInput(attrs={'class':'form-control'}),
                '售后':forms.Select(attrs={'class':'form-control'}),
                '类别':forms.Select(attrs={'class':'form-control'}),
                '型号':forms.Select(attrs={'class':'form-control'}),
                'sn':forms.TextInput(attrs={'class':'form-control'}),
                '故障描述':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入故障描述'}),
                '价格':forms.NumberInput(attrs={'class':'form-control','placeholder':'请输入价格'}),
                '数量':forms.NumberInput(attrs={'class':'form-control','placeholder':'请输入数量'}),
                '教室':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入教室'}),
                '方式':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入处理的方式'}),
                'asp':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入售后人员'}),
                'telephone':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入售后人员电话'}),
                '通知时间':forms.DateInput(attrs={'class':'form-control','type':'date'}),
                '到校时间':forms.DateInput(attrs={'class':'form-control','type':'date'}),
                '返校时间':forms.DateInput(attrs={'class':'form-control','type':'date'}),
                'scraped':forms.CheckboxInput(),
            }

class CustomerForm(forms.ModelForm):
    form_title = '售后单位'
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
                  'title':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入售后单位名称'}),
                  'group':forms.Select(attrs={'class':'form-control'})
            }

class Unit_typeForm(forms.ModelForm):
    form_title = '类别'
    class Meta:
        model = Unit_types
        fields = '__all__'
        widgets = {
                '设备类型':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入设备类型'}),
                'customer':forms.Select(attrs={'class':'form-control'})
            }

class Unit_modelForm(forms.ModelForm):
    form_title = '设备型号'
    class Meta:
        model = Unit_models
        fields = '__all__'
        widgets = {
                '设备类型':forms.Select(attrs={'class':'form-control'}),
                '型号':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入型号'}),
            }
        
class Report_timeForm(forms.ModelForm):
    class Meta:
        model = Report_time
        exclude = ['used']
        widgets = {
                'title':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入报账名称'}),
                'detail':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入备注'}),
                'report_time':forms.DateInput(attrs={'class':'form-control','type':'date'}),
                'customer':forms.Select(attrs={'class':'form-control'}),
            }

class LoginForm(forms.Form):
    username = forms.CharField(label = '用户名' , widget = forms.TextInput(attrs={'class':'form-control','placeholder':'请输入用户名'}))
    password = forms.CharField(label = '密码' , widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'请输入密码'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = auth.authenticate(username = username , password = password)
        if user is None:
            raise forms.ValidationError('用户名或密码错误')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data
