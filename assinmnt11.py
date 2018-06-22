ASSIGNMENT-9
#Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.
import threading 
from threading import Thread
import time
def display():
   for x in range(8):
       print(threading.current_thread().getName(),"hello world")   
       time.sleep(5)
t=Thread(target=display)
t.start()

#2 make a thread that print number from 1-10, waits for 1 sec between

import threading 
from threading import Thread
import time
def display():
   for x in range(10):
       time.sleep(1)
       print("the thread is ",x)
       
       
t=Thread(target=display)
t.start()



#3 create a list that has 5 element 
create a threading process that print the 5 element of the list with a delay of multiple of 2 sec between each display
x=

# int(input("enter any number"))
y=int(input("enter any number"))
z=int(input("enter any number"))
w=int(input("enter any number"))
v=int(input("enter any number"))
l=[x,y,z,w,v]
print(l)
import threading 
from threading import Thread
import time 
def display(n):
    d=2

    for l in n:

        time.sleep(d)
        d=d+2
        print("the thread is",l)
t=Thread(target=display,args=(l,))
t.start()





#4call a factorial function using threads.
import threading
from threading import Thread
import time
import math

def display():
    x=int(input("enter the no. :"))
    a=math.factorial(x)
    print("result:",a)
	
	
t=Thread(target=display)
t.start()