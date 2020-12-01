
import threading
from threading import*
import time
import Backendcode as x
x.create("freshworks",25)
x.create("frw",70,3600)
x.read("freshworks")
x.read("frw")
x.create("freshworks",50)
x.modify("freshworks",55)
x.delete("freshworks")

key_name=input('Enter key name:')
value=int(input('Enter value:'))
timeout=int(input('Enter stay time:'))

t1=threading.Thread(target=(x.create or x.read or x.delete),args=(key_name,value,timeout))
t1.start()
t1.join()

key_name=input('Enter key name:')
value=int(input('Enter value:'))
timeout=int(input('Enter stay time:'))

t2=threading.Thread(target=(x.create or x.read or x.delete),args=(key_name,value,timeout))
t2.start()
t2.join()
