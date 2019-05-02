#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ivan Vladimir Meza Ruiz 2018
# CARMEN Y YUMIN 2019
# GPL 3.0

import random
import datetime
import json

with open('/home/krmn/Documentos/IIMAS/chatvoice/conversations/kb.db','r') as f:
    data = f.readlines()

for x in data:
    json.dumps(x)
y = json.loads(x)





def execute(*args):
    var=args[0]
    opts=args[1]
    
    now = datetime.datetime.now()
    today12pm = now.replace(hour=12, minute=0, second=0, microsecond=0)
    today7pm = now.replace(hour=19, minute=0, second=0, microsecond=0)
    today12am = now.replace(hour=0, minute=0, second=0, microsecond=0)
    
    if now < today12pm : 
        msg = (random.choice(['Hola ','Buenos dias ']+opts)) + y['name']     #lista de saludo para horario de la ma;ana
    
    elif now < today7pm :
        msg = (random.choice(['Hola ','Buenas tardes ','Buen dia ']+opts))+y['name']
    
    else:
        msg = (random.choice(['Hola','Buenas noches']+opts)) + y['name']     #lista de saludo para horario de noche



    return 'set_slot {0} "{1}"'.format(var,msg)


f.close()