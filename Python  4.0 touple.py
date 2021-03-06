#!/usr/bin/env python
# coding: utf-8

# In[2]:


students = ("aaditya","Gauri","RAJ","Nandini","Sara")
print(students)
type(students)


# In[4]:


students[3] = "Siya"


# In[11]:


#Strings can be created using the simple quotes and double quotes
Name = "Jyoti"
Area = 'Sangli'


# In[12]:


text = """Python is an interpreted, high-level, general-purpose programming language. 
first released in 1991 , Python's design philosophy emphasizes code readability 
with its notable use of significant whitespace. Its language constructs and 
object-oriented approach aims to help programmers write clear, [] , . ss @  
logical code for small and large-scale projects."""


# In[14]:


print(text)


# In[16]:


text.lower()


# In[18]:


text_lower = text.lower()
print(text_lower)


# In[20]:


text.upper()


# In[22]:


text_upper = text.upper()
print(text_upper)


# In[24]:


text.split()


# In[26]:


text_split = text.split()
print(text_split)
type(text_split)
len(text_split)


# In[28]:


text.endswith('n')


# In[29]:


text.endswith('.')


# In[31]:


text_lower = text.lower()
print(text_lower)


# In[32]:


print(text_lower.capitalize())


# In[33]:


print(text_lower.title())


# In[35]:


text.endswith('s',0,6) # suffix,start and end


# In[36]:


text.endswith('s',0,9) # suffix,start and end


# In[38]:


text.count('ed') # count how many timesthe value present in the string


# In[39]:


text_lower.count('python')


# In[40]:


text.endswith('s',0,25)


# In[48]:


text.endswith('s',0,24)


# - string

# In[67]:


string1 = "My name is Jyoti and I am working a Data Scientist"


# In[68]:


print(string1)


# In[72]:


# Converting from a string to list
list1 = string1.split()


# In[73]:


print(list1)


# In[74]:


len(list1)


# In[78]:


list1.append('DL','AI')


# In[81]:


list1.append(['DL','AI']) # append takes only one argument so when you pass a list as an argument it considers it as only one element


# In[82]:


print(list1)


# In[85]:


list1.extend(['DL','AI']) # extend will consider all elementsin that list as seperate and extend can add multiple element


# In[86]:


print(list1)


# - A list is considered as a single element but contains multiple element within it.
# - So when you pass the list in append it takes it as a single element and creates a nested list 
# - In extend only the elements presentin list are added so you do not see nested list

# In[88]:


list1.insert(4,'Sabarad')


# In[90]:


print(list1)


# In[91]:


list1[3] = "Jyoti Sabarad"


# In[92]:


print(list1)


# In[95]:


list1.pop() # pop removes the last element in the list and tells which element has been removed


# In[118]:


list1.pop(4)


# In[112]:


print(list1)


# In[114]:


print(list.reverse())


# In[116]:


print(list1)


# In[120]:


list2 = ['A','B','C','D']


# In[122]:


print(list2.reverse())


# In[126]:


print(list2)


# - Create a tuple with any six states of an India and apply append,extend,pop,reverse.

# In[131]:


list3 = ("Maharashtra","Karnataka","Goa","Rajasthan","Hariyana","Punjab")
print(list3)
type(list3)


# In[134]:


list3 = tuple(list3) # I have converted my list to tuple using tuple function
type(list3)


# In[136]:


print(list3)


# In[137]:


list3 = list(list3) # Converting my tiple to list using list() function


# In[139]:


type(list3)


# In[ ]:


tuple1 = () # To initialize a tuple
list = [] # To Initialize a list

