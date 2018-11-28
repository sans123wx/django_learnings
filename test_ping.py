import os
from datetime import *
from monitor.models import * 

while True:
    connect = os.system('ping 10.255.254.25')
    if connect :
        starttime = datetime.now()
        date = date.today()
        monitor = Monitor()
        monitor.name = '深信服外网防火强'
        monitor.ip = '10.255.254.25'
        monitor.date = date
        monitor.startime = starttime
        monitor.save()
        while True:
            connect2 = os.system('ping 10.255.254.25')
            if  not connect2:
                endtime = datetime.now()
                used_time = endtime - starttime
                monitor.endtime = endtime
                monitor.used_time = used_time
                monitor.save()
                break
                
                
