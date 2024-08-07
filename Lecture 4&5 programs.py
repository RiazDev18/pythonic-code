#!/usr/bin/env python
# coding: utf-8

# In[1]:

magic = 3

# In[2]:


type(magic)


# In[3]:


trick = 1.5


# In[4]:


type(trick)


# In[5]:


trick2 = magic / trick


# In[6]:


print(trick2)


# In[7]:


type(trick2)


# In[8]:


trick2 = int(trick2)

type(trick2)


# In[10]:


print(trick2)


# In[12]:


x = float(1)
type(x)


# In[14]:


y = int('2')
type(y)


# In[15]:


z=str(6.3)
type(z)


# In[16]:


# These are the exmple of strings


# In[17]:


example1 = 'This is a string'
example2 = 'And this also a string'
print(example1)
print(example2)


# In[18]:


type(example1)


# In[22]:


vulcan, salute = 'Live Long', 'Prosper'
print(vulcan + ' and ' + salute)


# In[27]:


print(vulcan + str(magic))


# In[29]:


print(vulcan + ' and ' + 3*(salute + ' '))


# In[26]:


# These are programming examples of Complex numbers

z = 42+24j
print(z)


# In[30]:


x, y = complex(1, 2), complex(3, 4)


# In[31]:


print('Addition =', x + y)
print('Subtraction =', x - y)
print('Multiplication =', x * y)
print('Division =', x / y)
print('Conjugate =', x.conjugate())


# In[33]:


# The programming examples of Lists

numbers = [1, 2, 3, 4, 5]
vulcan = ['wuhkuh', 'dahkuh', 'rehkuh',
          'kehkuh', 'kaukuh']
starships = [1701, 'Enterprise', 1278.40, 
             1031, 'Discovery', 1207.3] 


# In[34]:


print(numbers[0])
print(vulcan[2:4]) 


# In[36]:


scifi = ['S','t','a','r','T','r','e','k']
scifi[4]


# In[37]:


scifi[4:] = 'W','a','r','s'
print(scifi) 


# In[38]:


scifi.append('.')
print(scifi)


# In[ ]:




