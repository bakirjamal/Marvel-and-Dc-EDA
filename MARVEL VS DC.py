#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as  plt


# In[2]:


marvel=pd.read_csv("charcters_stats.csv")


# In[3]:


marvel.head()


# In[4]:


marvel.shape


# In[5]:


marvel["Alignment"].value_counts()


# In[6]:


marvel[marvel["Alignment"]=="good"]


# In[7]:


good=marvel[marvel["Alignment"]=="good"]


# In[8]:


good.head()


# In[9]:


good.sort_values(by=["Speed"],ascending=False).head()


# In[10]:


good.sort_values(by=["Power"],ascending=False).head()


# In[11]:


good_power_max_full=good[good["Power"]==100]


# In[12]:


good_power_max_full.shape


# In[13]:


good_power_max_full


# In[14]:


good_max_power=good.sort_values(by=["Total"],ascending=False)


# In[15]:


good_max_power.head()


# In[16]:


plt.figure(figsize=(5,7))
plt.bar(list(good_max_power["Name"].sort_values()[0:5]),list(good_max_power["Total"].sort_values()[0:5]),color=["red","yellow","blue","green","orange"])
plt.show()


# In[17]:


bad=marvel[marvel["Alignment"]=="bad"]


# In[18]:


bad.head()


# In[19]:


bad.sort_values(by=["Durability"],ascending=False)


# In[20]:


bad.sort_values(by=["Power"],ascending=False)


# In[21]:


bad.sort_values(by=["Speed"],ascending=False)


# In[22]:


bad.sort_values(by=["Intelligence"],ascending=False)


# In[23]:


bad.sort_values(by=["Total"],ascending=False)


# In[24]:


bad_max_full=bad.sort_values(by=["Total"],ascending=False)


# In[25]:


bad_max_full.head()


# In[26]:


plt.figure(figsize=(8,5))
plt.bar(list(bad_max_full["Name"].sort_values()[0:5]),list(bad_max_full["Total"].sort_values()[0:5]),color=["red","yellow","black","blue","green"])
plt.show()


# In[27]:


plt.figure(figsize=(8,5))
plt.hist(good["Speed"])
plt.title("DISTREBUTION OF SPEED")
plt.xlabel("speed")
plt.show()


# In[28]:


plt.figure(figsize=(10,5))
plt.hist(bad["Combat"])
plt.title("DISTREBUTION OF COMBAT")
plt.xlabel("COMBAT")
plt.show()


# In[ ]:




