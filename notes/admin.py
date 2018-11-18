from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    fields = ('date','类别','型号','故障描述','价格','数量','教室','方式','售后','报账时间','报账','owner')
    list_display = ('date','类别','型号','故障描述','价格','数量','合计','教室','方式','售后','报账时间','报账','owner')
#    list_editable = ('owner',)
    
@admin.register(Unit_models)
class Unit_modelsAdmin(admin.ModelAdmin):
    list_display = ('id','型号','设备类型')

@admin.register(Report_time)
class Report_timeAdmin(admin.ModelAdmin):
    list_display = ('id','title','report_time','detail','customer')

@admin.register(Unit_types)
class Unit_typesAdmin(admin.ModelAdmin):
    list_display = ('id','设备类型')    
admin.site.register([Customer])

