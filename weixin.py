import requests
import time
import random
import hashlib
for i in range(1,1000):
    a=random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890')
    b=random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890')
    c=random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890')
    strings=a+b+c
    m=hashlib.md5()
    m.update(strings)
    crestr=m.hexdigest()
    url='http://vcloud1023.tc.qq.com/1023_'+crestr+'.f0.mp4'
    r=requests.get(url)
    if r.status_code==200:
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",url
    else:
        print r.status_code,strings,crestr

