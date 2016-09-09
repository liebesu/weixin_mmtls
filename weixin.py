import requests
import time
import random
import hashlib
from multiprocessing import Pool

def weixin(i):
    a=random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890')
    b=random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890')
    c=random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890')
    d=random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890')
    e=random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890')
    f=random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890')
    strings=a+b+c+d+e+f
    m=hashlib.md5()
    m.update(strings)
    crestr=m.hexdigest()
    url='http://vcloud1023.tc.qq.com/1023_'+crestr+'.f0.mp4'
    r=requests.get(url)
    if r.status_code==200:
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",url
        z=open('have.txt','a')
        z.write(url+"\n")
        z.close()
    else:
        print r.status_code,strings,crestr


if __name__=="__main__":
    pool = Pool(processes=50)
    pool.map(weixin,range(1,100000))
    pool.join()
    pool.close()


