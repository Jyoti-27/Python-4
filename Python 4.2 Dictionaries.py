#!/usr/bin/env python
# coding: utf-8

# - Dictionaries

# In[1]:


states_capitals = {"Telangana":"Hyderabad","AP":"Amaravati","Haryana":"Chandigarh","Meghalaya":"Shillang","UP":"Lucknow"}


# In[3]:


type(states_capitals)


# In[5]:


print(states_capitals)


# In[6]:


states_cities = {"Telangana":["Hyderabad","Secunderabad"],"AP":["Amaravati","Vizag"],"Haryana":["Chandigarh","Rohtak",]}


# In[8]:


print(states_cities)


# In[10]:


capital = {["punjab","haryana"]:"chandigarh"}


# In[13]:


states_capitals.items()


# In[15]:


states_capitals.keys()


# In[17]:


states_capitals.values()


# In[19]:


states_capitals[1]


# In[21]:


# Fetch the values using keys
states_capitals["Telangana"]


# In[22]:


states_cities["Telangana"]


# In[31]:


states_capitals.update({"Assam":"Dispur"})


# In[30]:


print(states_cities)


# In[ ]:




