#!/usr/bin/env python
# coding: utf-8

# In[1]:


nums=[23,34,54,12,43]

Result=list(map(lambda n: n*7,nums))
print(Result)


# In[2]:


Evens=list(filter(lambda n: n%2==0,nums))
print(Evens)


# In[7]:


hum=[12,23,34,45,56]
End=list(map(lambda n :n*2,hum))
print(End)


# In[8]:


sample=[34,45,56,67,78,45,56]


# In[9]:


Calculate=list(map(lambda n: n+34,sample))
print(Calculate)


# In[ ]:




