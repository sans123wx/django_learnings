from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User , Group
from django.shortcuts import Http404

# Create your models here.

class Customer(models.Model):
    title = models.CharField(max_length = 30 ,verbose_name = '售后单位')
    group = models.ForeignKey(Group , on_delete = models.DO_NOTHING , verbose_name = '负责部门')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '售后单位'
        verbose_name_plural = '售后单位'

class Unit_types(models.Model):
    设备类型 = models.CharField(max_length = 30)
    customer = models.ForeignKey(Customer,on_delete = models.DO_NOTHING,verbose_name = '售后单位')

    def __str__(self):
        return self.设备类型

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = '类别'
    
class Unit_models(models.Model):
    设备类型 = models.ForeignKey(Unit_types,on_delete = models.DO_NOTHING)
    型号 = models.CharField(max_length = 30)

    def __str__(self):
        return self.型号

    class Meta:
        verbose_name = '设备型号'
        verbose_name_plural = '设备型号'

class Report_time(models.Model):
    title = models.CharField(max_length = 30,verbose_name = '名称')
    detail = models.CharField(max_length = 30 , default = '无' , verbose_name = '备注')
    report_time = models.DateField(verbose_name = '报账时间')
    customer = models.ForeignKey(Customer , on_delete = models.DO_NOTHING , verbose_name = '售后')
    used = models.BooleanField(default = False , verbose_name = '是否已使用')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '报账时间'
        verbose_name_plural = '报账时间'
        ordering = ['-report_time']  
    
class Notes(models.Model):
    date = models.DateField(default = timezone.now)
    类别 = models.ForeignKey(Unit_types , on_delete = models.DO_NOTHING)
    型号 = models.ForeignKey(Unit_models , on_delete = models.DO_NOTHING)
    故障描述 = models.CharField(max_length = 30)
    价格 = models.IntegerField()
    数量 = models.IntegerField()
    教室 = models.CharField(max_length = 30)
    报账 = models.BooleanField()
    方式 = models.CharField(max_length = 30)
    售后 = models.ForeignKey(Customer,on_delete = models.DO_NOTHING)
    状态 = models.CharField(max_length = 15 , default = '未通知售后')
    通知时间 = models.DateField(blank = True , null = True)
    到校时间 = models.DateField(blank = True , null = True)
    返校时间 = models.DateField(blank = True , null = True)
    响应时间 = models.DurationField(blank = True , null = True)
    修复时间 = models.DurationField(blank = True , null = True)
    报账时间 = models.ForeignKey(Report_time,on_delete = models.DO_NOTHING,blank = True , null = True)
    合计 = models.IntegerField(blank = True , null = True)
    owner = models.ForeignKey(User,on_delete = models.DO_NOTHING)
    sn = models.CharField(max_length = 30,blank = True , null = True , default = '无' , verbose_name = '序列号')
    asp = models.CharField(max_length = 30,blank = True , null = True , verbose_name = '售后人员')
    telephone = models.CharField(max_length = 30,blank = True , null = True , verbose_name = '售后电话')
    scraped = models.BooleanField(default = False , verbose_name = '是否报废')
    

    def __str__(self):
        return self.类别.设备类型

    def save(self):
        self.合计 = self.价格 * self.数量
        self.状态 = '未通知售后'
        if self.通知时间:self.状态 = '已通知售后'   
        if self.到校时间:
            if not self.通知时间:
                raise Http404
            else:
                self.状态 = '设备已返厂'
                self.响应时间 = self.到校时间 - self.通知时间
        if self.返校时间:
            if not self.到校时间:
                raise Http404
            elif not self.scraped:
                self.状态 = '设备已修复'
                self.修复时间 = self.返校时间 - self.到校时间
            else:
                self.状态 = '设备报废'
        super().save()
        

    class Meta:
        ordering = ['-date']
        verbose_name = '维修记录'
        verbose_name_plural = '维修记录'
        
