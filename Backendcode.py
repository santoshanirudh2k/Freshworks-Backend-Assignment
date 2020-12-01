import threading
from threading import*
import time
a={}
def create(key,value,timeout=0):
    if key in a:
        print("error: this key already exists")
    else:
        if(key.isalpha()):
            if len(a)<(1024*1020*1024) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32:
                    a[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")

def read(key):
    if key not in a:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b=a[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0])
                return stri
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri

def delete(key):
    if key not in a:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b=a[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del a[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            del a[key]
            print("key is successfully deleted")

def modify(key,value):
    if key not in a:
        print("error: given key does not exist in database. Please enter a valid key") #error message6
    else:
        b=a[key]
        if b[1]!=0:
            if time.time()<b[1]:
                l=[]
                l.append(value)
                l.append(b[1])
                a[key]=l
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            a[key]=l
