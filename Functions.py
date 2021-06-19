#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Functions


# In[2]:


#Defining a function


# In[3]:


def function():
    print('Hello')


# In[4]:


function()


# In[5]:


def areaofcircle():
    radius=int(input('Enter the value'))
    pi=3.14
    Area=pi*(radius**2)
    print(Area,'is the area of the circle')


# In[6]:


areaofcircle()


# In[11]:


def areaofrectangle():
    Length=int(input('Enter the length'))
    Breadth=int(input('Enter the Breadth'))
    Area=Length*Breadth
    print(Area,'Area of rectangle')


# In[12]:


areaofrectangle()


# In[13]:


areaofrectangle()


# In[1]:


#Global variable , will retain the value in the entire Jupyter.
#Local variable will be born and die within a function


# In[3]:


def Range():
    for i in range(4):
        print(i)


# In[6]:


Range()


# In[29]:


def looptest():
    i=int(input('Enter the number'))
    if i%2==0:
        print('The number is even')
    else:
        print('The number is odd')


# In[30]:


looptest()


# In[33]:


#Calling function from inside the function


# In[34]:


def loopcall():
    print('trying to call the function')
    looptest()


# In[35]:


loopcall()


# In[36]:


#Parametric Functions


# In[37]:


def Parafunc(a,b):
    c=a+b
    print(c,'is the result of addition')


# In[38]:


Parafunc(45,67)


# In[39]:


def Parafunc2(pi,r,t):
    Multi=(pi*r*t)
    print(Multi,'is the expected answer')


# In[41]:


Parafunc2(23,45,678)


# In[1]:


def parafunc3(a,b,c):
    c=a*b*c
    print(c)


# In[2]:


parafunc3(23,45,56)


# In[ ]:


#Defining function using Arguments


# In[3]:


def arg(*args):
    return sum(args)


# In[4]:


arg(23,34)


# In[7]:


def arg2(*args):
    return max(args)


# In[8]:


arg2(23,34,45,67,3455555,45)


# In[9]:


#point to note, whenever a Function is used, return statement can be used, whereas for a for loop break function can be used.


# In[27]:


#with print end=''
def test():
    for i in range(10):
        if i==5:
            return
        print(i,end="")


# In[28]:


test()


# In[33]:


#without print end=""
def test():
    for i in range(20):
        if i==5:
            return
        print(i)
            


# In[34]:


test()


# In[59]:


def tst(arg1,arg2):
    c=arg1+arg2
    return c


# In[60]:


tst(34,56)


# In[61]:


rec=tst(34,56)
print('total',rec)


# In[62]:


#Using anonymous function


# In[65]:


first=lambda x:x*2
first(6)


# In[67]:


second=lambda x,y,z:x*y*z
second(23,34,45)


# In[68]:


third=lambda w,r,a:(w+r)*a
third(34,56,89)


# In[69]:


#Using anonymous function using map


# In[72]:


t=[12,334,56,67]
list(map(lambda x:x*2,t))


# In[74]:


round(23.444444444,4)


# In[75]:


#Error handling
57/0


# In[78]:


try:
    57/0
except ZeroDivisionError as err:
        print('Handling the error',err)


# In[79]:


def div():
    a=23
    b=0
    c=a/b
    print(c)


# In[83]:


try:
    div()
except ZeroDivisionError as err:
    print('Handling the exception',err)


# In[84]:


def div1():
    d=23
    t=0
    c=d/t
    print(c)


# In[86]:


try:
    div1()
except ZeroDivisionError as err:
    print('Handling error',err)


# In[90]:


def high(x,y):
    try:
        result=x/y
    except ZeroDivisionError as err:
        print('Handling the exception',err)
    else:
        print('The value',result)
    finally:
        print('It is executed')


# In[92]:


high(34,0)


# In[93]:


#C style string formatting


# In[96]:


name='Neeraj'
print('Hello',name,'!')


# In[98]:


name='Neerajazz'
print('Hello',"%s !",% name)


# In[100]:


name='Jelly'
Age=34
print("The name of the person is {} and his age is {}".format(name,Age))


# In[105]:


Model='HImalayan'
Engine=400
print("The model of the bike is {} and its cc is {}".format(Model,Engine))


# In[ ]:




