#!/usr/bin/env python
# coding: utf-8

# In[2]:


string1 = "My name is Jyoti and I am working a Data Scientist"


# In[4]:


print(string1)


# In[5]:


# Converting from a string to list
list1 = string1.split()


# In[7]:


print(list1)


# In[9]:


len(list1)


# In[15]:


list1.append('DL','AI')


# In[13]:


list1.append(['DL','AI']) # append takes only one argument so when you pass a list as an argument it considers it as only one element


# In[16]:


print(list1)


# In[17]:


list1.insert(4,'Sabarad')


# In[19]:


print(list1)


# In[20]:


list1[3] = "Jyoti Sabarad"


# In[22]:


print(list1)


# In[46]:


list1.pop(2)


# In[52]:


list2 = ['A','B','C','D']


# In[54]:


print(list2.reverse())


# In[56]:


print(list2.reverse())
print(list2)


# In[65]:


list3 = ["Maharashtra","Karnataka","Goa","Rajasthan","Hariyana","Punjab"]
print(list3)
type(list3)


# In[60]:


list3 = tuple(list3) # I have converted my list to tuple using tuple function
type(list3)


# In[61]:


print(list3)


# In[63]:


list3 = list(list3) # Converting my tiple to list using list() function
type(list3)


# In[66]:


tuple1 = () # To initialize a tuple
list = [] # To Initialize a list


# In[70]:


list3 = ["Maharashtra","Karnataka","Goa","Rajasthan","Hariyana","Punjab"]
print(list3.reverse())
print(list3)


# In[71]:


list3.pop(3)
print(list3)


# In[ ]:




