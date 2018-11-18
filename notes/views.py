from django.shortcuts import get_object_or_404 , render , redirect , Http404
from .models import *
from django.db.models import Sum,Count
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.forms import modelformset_factory
from .default_settings import *

# Create your views here.   

def wbz(request):
    contents = Notes.objects.filter(报账=False)
    prices = contents.aggregate(total = Sum('合计'))['total']
    counts = Unit_types.objects.filter(notes__报账=False).annotate(total=Sum('notes__数量'),total_p=Sum('notes__合计'))
    context = {}
    context['counts'] = counts
    context['prices'] = prices
    context['contents'] = contents
    return render(request,'home.html',context)

def ybz_detail(request,rtl_id):
    title = get_object_or_404(Report_time,id = rtl_id).title
    contents = Notes.objects.filter(报账时间=rtl_id)
    prices = contents.aggregate(total = Sum('合计'))['total']
    counts = Unit_types.objects.filter(notes__报账时间=rtl_id).annotate(total=Sum('notes__数量'),total_p=Sum('notes__合计'))
    context = {}
    context['title'] = title
    context['counts'] = counts
    context['contents'] = contents
    context['prices'] = prices
    return render(request,'ybz_detail.html',context)

def print_page(request,user_id):
    if request.user.id != user_id:
        raise Http404('兄弟，别乱搞')
    notes_id = request.POST.getlist('note')
    notes = [Notes.objects.get(id = x) for x in notes_id]
    total_price = sum([x.合计 for x in notes])
    context = {}
    context['notes'] = notes
    context['total_price'] = total_price
    return render(request,'print_page.html',context)

def report_time_list(request):
    report_time_lists = Report_time.objects.all()
    total_price = Report_time.objects.dates('report_time','year')
    context = {}
    context['report_time_lists'] = report_time_lists
    context['total_price'] = total_price
    return render(request,'report_time_list.html',context)

def new_note(request,user_id):
    if request.user.id != user_id:
        raise Http404('兄弟，别乱搞')
    owner = get_object_or_404(User,id = user_id)
    groups = owner.groups.all()
    group_id = request.GET.get('group')
    group = get_object_or_404(Group , id = group_id)
    if group not in groups:
        raise Http404('没有权限')
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form_new = form.save(commit = False)
            form_new.owner = owner
            form_new.报账 = False
            form_new.save()
            return redirect(reverse('user_admin' , args=[request.user.id]))
    else:       
        form = NoteForm()
        form.fields['售后'].queryset = Customer.objects.filter(group = group)
        form.fields['类别'].queryset = Unit_types.objects.filter(customer__group = group)
        form.fields['型号'].queryset = Unit_models.objects.filter(设备类型__customer__group = group)
        context = {}
        context['form'] = form
        context['group'] = group
        return render(request,'new_note.html',context)

def management(request , user_id):
    if request.user.id != user_id:
        raise Http404('兄弟，别乱搞')
    owner = get_object_or_404(User,id = user_id)
    groups = owner.groups.all()
    group_id = request.GET.get('group')
    group_bz = get_object_or_404(Group , id = 5)
    group = get_object_or_404(Group , id = group_id)
    if group_bz not in groups or group not in groups:
        raise Http404('没有权限')
    context = {}
    context['group_id'] = request.GET.get('group')
    return render(request , 'management.html' , context)

def management_customers(request , user_id):
    customers = Customer.objects.filter(group__user__id = user_id)
    context = {}
    context['others'] = customers
    context['title'] = '管理售后单位'
    context['urls'] = 'new_customer'
    context['urls_c'] = 'edit_customer'
    context['group_id'] = request.GET.get('group')
    return render(request , 'management_others.html' , context)

def management_unit_types(request , user_id):
    unit_types = Unit_types.objects.filter(customer__group__user__id = user_id)
    context = {}
    context['others'] = unit_types
    context['title'] = '管理设备类型'
    context['urls'] = 'new_unit_type'
    context['urls_c'] = 'edit_unit_type'
    context['group_id'] = request.GET.get('group')
    return render(request , 'management_others.html' , context)

def management_unit_models(request , user_id):
    unit_models = Unit_models.objects.filter(设备类型__customer__group__user__id = user_id)
    context = {}
    context['others'] = unit_models
    context['title'] = '管理设备型号'
    context['urls'] = 'new_unit_model'
    context['urls_c'] = 'edit_unit_model'
    context['group_id'] = request.GET.get('group')
    return render(request , 'management_others.html' , context)

def new_customer(request , user_id):
    if request.user.id != user_id:
        raise Http404('兄弟，别乱搞')
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_admin' , args=[request.user.id]))
    else:
        group_id = request.GET.get('group')
        form = CustomerForm()
        form.fields['group'].queryset = Group.objects.filter(id = group_id)
        context = {}
        context['form'] = form
        context['urls'] = 'new_customer'
        return render(request , 'new_others.html' , context)

def edit_customer(request , customer_id):
    customer = Customer.objects.get(id = customer_id)
    group = customer.group
    if request.method != 'POST':
        form = CustomerForm(instance = customer)
        form.fields['group'].queryset = Group.objects.filter(id = group.id)
    else:
        form = CustomerForm(instance = customer , data = request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_admin' , args=[request.user.id]))
    context = {}
    context['form'] = form
    context['note'] = customer
    context['urls_c'] = 'edit_customer'
    return render(request , 'edit_note.html' , context)

def new_unit_type(request , user_id):
    if request.user.id != user_id:
        raise Http404('兄弟，别乱搞')
    if request.method == 'POST':
        form = Unit_typeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_admin' , args=[request.user.id]))
    else:
        form = Unit_typeForm()
        form.fields['customer'].queryset = Customer.objects.filter(group__id = request.GET.get('group'))
        context = {}
        context['form'] = form
        context['urls'] = 'new_unit_type'
        return render(request , 'new_others.html' , context)

def edit_unit_type(request , unit_type_id):
    unit_type = Unit_types.objects.get(id = unit_type_id)
    if request.method != 'POST':
        form = Unit_typeForm(instance = unit_type)
        form.fields['customer'].queryset = Customer.objects.filter(group__id = request.GET.get('group'))
    else:
        form = Unit_typeForm(instance = unit_type , data = request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_admin' , args=[request.user.id]))
    context = {}
    context['form'] = form
    context['note'] = unit_type
    context['urls_c'] = 'edit_unit_type'
    return render(request , 'edit_note.html' , context)
    
def new_unit_model(request , user_id):
    if request.user.id != user_id:
        raise Http404('兄弟，别乱搞')
    if request.method == 'POST':
        form = Unit_modelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_admin' , args=[request.user.id]))
    else:
        form = Unit_modelForm()
        form.fields['设备类型'].queryset = Unit_types.objects.filter(customer__group__id = request.GET.get('group'))
        context = {}
        context['form'] = form
        context['urls'] = 'new_unit_model'
        return render(request , 'new_others.html' , context)

def edit_unit_model(request , unit_model_id):
    unit_model = Unit_models.objects.get(id = unit_model_id)
    if request.method != 'POST':
        form = Unit_modelForm(instance = unit_model)
        form.fields['设备类型'].queryset = Unit_types.objects.filter(customer__group__id = request.GET.get('group'))
    else:
        form = Unit_modelForm(instance = unit_model , data = request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_admin' , args=[request.user.id]))
    context = {}
    context['form'] = form
    context['note'] = unit_model
    context['urls_c'] = 'edit_unit_model'
    return render(request , 'edit_note.html' , context)

def edit_note(request , note_id):
    note = Notes.objects.get(id = note_id)
    group = note.售后.group
    if request.method != 'POST':
        form = NoteForm(instance = note)
        form.fields['售后'].queryset = Customer.objects.filter(group = group)
        form.fields['类别'].queryset = Unit_types.objects.filter(customer__group = group)
        form.fields['型号'].queryset = Unit_models.objects.filter(设备类型__customer__group = group)
    else:
        form = NoteForm(instance = note , data = request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_admin' , args=[request.user.id]))
    context = {}
    context['form'] = form
    context['note'] = note
    context['urls_c'] = 'edit_note'
    return render(request , 'edit_note.html' , context)

def delete_note(request , note_id):
    note = Notes.objects.get(id = note_id)
    note.delete()
    return redirect(reverse('user_admin' , args=[request.user.id]))

def user_admin(request,user_id):
    if request.user.id != user_id:
        raise Http404('兄弟，别乱搞')
    owner = get_object_or_404(User,id = user_id)
    notes = Notes.objects.filter(owner = owner , 报账 = False)
    counts = Unit_types.objects.filter(notes__报账=False , notes__owner = owner).annotate(total=Sum('notes__数量'),total_p=Sum('notes__合计'))
    prices = notes.aggregate(total = Sum('合计'))['total']
    context = {}
    context['notes'] = notes
    context['prices'] = prices
    context['counts'] = counts
    return render(request,'user_admin.html',context)

def user_admin_ybz(request,user_id):
    if request.user.id != user_id:
        raise Http404('兄弟，别乱搞')
    owner = get_object_or_404(User,id = user_id)
    notes = Notes.objects.filter(owner = owner , 报账 = True)
    counts = Unit_types.objects.filter(notes__报账=True , notes__owner = owner).annotate(total=Sum('notes__数量'),total_p=Sum('notes__合计'))
    prices = notes.aggregate(total = Sum('合计'))['total']
    groups = owner.groups.all()
    customers = [x for i in groups for x in i.customer_set.all()]
    context = {}
    context['notes'] = notes
    context['prices'] = prices
    context['counts'] = counts
    context['customers'] = customers
    return render(request,'user_admin_ybz.html',context)

def report_customer(request , user_id):
    if request.user.id != user_id:
        raise Http404('兄弟，别乱搞')
    owner = get_object_or_404(User,id = user_id)
    groups = owner.groups.all()
    group_id = request.GET.get('group')
    group_bz = get_object_or_404(Group , id = 5)
    group = get_object_or_404(Group , id = group_id)
    if group_bz not in groups or group not in groups:
        raise Http404('没有权限')
    customers = Customer.objects.filter(group = group)
    context = {}
    context['customers'] = customers
    context['group'] = group
    return render(request , 'report_customer.html' , context)    
    
def report(request , user_id):
    if request.user.id != user_id:
        raise Http404('兄弟，别乱搞')
    owner = get_object_or_404(User,id = user_id)
    groups = owner.groups.all()
    group_id = request.GET.get('group')
    group_bz = get_object_or_404(Group , id = 5)
    group = get_object_or_404(Group , id = group_id)
    if group_bz not in groups or group not in groups:
        raise Http404('没有权限')
    notes = Notes.objects.filter(报账 = False , 售后__id = request.GET.get('customer'))
    report_times = Report_time.objects.filter(customer__group = group)
    context = {}
    context['notes'] = notes
    context['report_times'] = report_times
    context['group'] = group
    return render(request , 'report.html' , context)

def report_bz(request , user_id):
    if request.user.id != user_id:
        raise Http404('兄弟，别乱搞')
    if request.method == 'POST':
        notes_id = request.POST.getlist('note')
        report_time_id = request.POST.get('report_time')
        report_time = get_object_or_404(Report_time , id = report_time_id)
        for note_id in notes_id:
            note = get_object_or_404(Notes , id = note_id)
            note.报账时间 = report_time
            note.报账 =  True
            note.save()
        return redirect(reverse('ybz'))

def new_report_time(request , user_id):
    if request.user.id != user_id:
        raise Http404('兄弟，别乱搞')
    owner = get_object_or_404(User,id = user_id)
    groups = owner.groups.all()
    group_id = request.GET.get('group')
    group_bz = get_object_or_404(Group , id = 5)
    group = get_object_or_404(Group , id = group_id)
    if group_bz not in groups or group not in groups:
        raise Http404('没有权限')
    if request.method == 'POST':
        form = Report_timeForm(request.POST)
        if form.is_valid():
            customer_id = form.cleaned_data['customer'].id
            form.save()
            return redirect(reverse('report' , args=[user_id]) + '?group=' + group_id + '&customer=' + str(customer_id))
    else:
        form = Report_timeForm()
        form.fields['customer'].queryset = Customer.objects.filter(group = group)
        context = {}
        context['form'] = form
        context['group'] = group
        return render(request , 'new_report_time.html' , context)

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))
