from django.shortcuts import get_object_or_404 , render , redirect , Http404
from .models import *
from django.db.models import Sum,Count
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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

def print_page(request,cust):
    contents_all = Notes.objects.filter(售后=cust,报账=True)
    context = {}
    context['contents'] = contents_all
    return render(request,'print.html',context)

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
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form_new = form.save(commit = False)
            form_new.owner = owner
            form_new.报账 = False
            form_new.save()
            return redirect(reverse('user_admin' , args=[request.user.id]))
    else:
        groups = owner.groups.all()
        form_dict = {'dj':{
                            '蓝鸽':[
                                    NoteForm_dj(initial={'类别':1 , '型号':1 , '故障描述':2 ,'价格':525 , '数量':1 , '方式':'跟换电源板' , '售后':1}),
                                    NoteForm_dj(initial={'类别':2 , '型号':2 , '故障描述':6 ,'价格':290 , '数量':1 , '方式':'返厂维修' , '售后':1}), 
                                   ],
                            '志向':[
                                    NoteForm_dj(initial={'类别':5 , '型号':5 , '故障描述':5 ,'价格':180 , '数量':1 , '方式':'光路除尘' , '售后':2}),
                                   ],
                            '空表':[
                                    NoteForm_dj()
                                    ]
                       
                           },
                      'wl':{
                            '大金':[
                                    NoteForm_wl()
                                    ],
                            '空表':[
                                   NoteForm_wl()
                                   ]
                           }                                 
                    }
        form_list = [form_dict[i.name] for i in groups]
        context = {}
        context['list'] = zip(groups,form_list)
        return render(request,'new_note.html',context)

def management(request , user_id):
    if request.user.id != user_id:
        raise Http404('兄弟，别乱搞')
    return render(request , 'management.html')

def management_customers(request , user_id):
    customers = Customer.objects.filter(group__user__id = user_id)
    context = {}
    context['others'] = customers
    context['title'] = '管理售后单位'
    context['urls'] = 'new_customer'
    context['urls_c'] = 'edit_customer'
    return render(request , 'management_others.html' , context)

def management_unit_types(request , user_id):
    unit_types = Unit_types.objects.filter(customer__group__user__id = user_id)
    context = {}
    context['others'] = unit_types
    context['title'] = '管理设备类型'
    context['urls'] = 'new_unit_type'
    context['urls_c'] = 'edit_unit_type'
    return render(request , 'management_others.html' , context)

def management_unit_models(request , user_id):
    unit_models = Unit_models.objects.filter(设备类型__customer__group__user__id = user_id)
    context = {}
    context['others'] = unit_models
    context['title'] = '管理设备型号'
    context['urls'] = 'new_unit_model'
    context['urls_c'] = 'edit_unit_model'
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
        groups = Group.objects.filter(user = user_id)
        form_dict = {x.name:CUSTOMER_FORM_DICT[x.name] for x in groups}
        context = {}
        context['form_dict'] = form_dict
        context['urls'] = 'new_customer'
        return render(request , 'new_others.html' , context)

def edit_customer(request , customer_id):
    customer = Customer.objects.get(id = customer_id)
    group = customer.group.name
    if request.method != 'POST':
        form = CUSTOMER_FORM_CLASS_DICT[group](instance = customer)
    else:
        form = CUSTOMER_FORM_CLASS_DICT[group](instance = customer , data = request.POST)
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
        groups = Group.objects.filter(user = user_id)
        form_dict = {x.name:UNIT_TYPE_FORM_DICT[x.name] for x in groups}
        context = {}
        context['form_dict'] = form_dict
        context['urls'] = 'new_unit_type'
        return render(request , 'new_others.html' , context)

def edit_unit_type(request , unit_type_id):
    unit_type = Unit_types.objects.get(id = unit_type_id)
    group = unit_type.customer.group.name
    if request.method != 'POST':
        form = UNIT_TYPE_FORM_CLASS_DICT[group](instance = unit_type)
    else:
        form = UNIT_TYPE_FORM_CLASS_DICT[group](instance = unit_type , data = request.POST)
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
        groups = Group.objects.filter(user = user_id)
        form_dict = {x.name:UNIT_MODEL_FORM_DICT[x.name] for x in groups}
        context = {}
        context['form_dict'] = form_dict
        context['urls'] = 'new_unit_model'
        return render(request , 'new_others.html' , context)

def edit_unit_model(request , unit_model_id):
    unit_model = Unit_models.objects.get(id = unit_model_id)
    group = unit_model.设备类型.customer.group.name
    if request.method != 'POST':
        form = UNIT_MODEL_FORM_CLASS_DICT[group](instance = unit_model)
    else:
        form = UNIT_MODEL_FORM_CLASS_DICT[group](instance = unit_model , data = request.POST)
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
    group = note.售后.group.name
    if request.method != 'POST':
        form = NOTE_FORM_CLASS_DICT[group](instance = note)
    else:
        form = NOTE_FORM_CLASS_DICT[group](instance = note , data = request.POST)
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
