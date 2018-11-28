from django.db import models

# Create your models here.

class Monitor(models.Model):
    name = models.CharField(max_length = 20 , verbose_name = '设备名称')
    ip = models.CharField(max_length = 30 , verbose_name = 'ip地址')
    date = models.DateField(verbose_name = '日期')
    startime = models.DateTimeField(blank = True , null = True , verbose_name = '开始时间')
    endtime = models.DateTimeField(blank = True , null = True , verbose_name = '结束时间')
    used_time = models.DurationField(blank = True , null = True , verbose_name = '持续时间')
    class Meta:
        ordering = ['-date']
        verbose_name = '断网记录'
        verbose_name_plural = '断网记录'
