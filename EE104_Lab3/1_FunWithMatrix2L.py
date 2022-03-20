#!/usr/bin/env python
# coding: utf-8

# In[1]:
import numpy as np
# In[5]:
rv=np.array([ [20,-15],[-15,25]])
# In[6]:
rv
# In[7]:
irv=np.linalg.inv(rv)
# In[8]:
irv
# In[11]:
vs=np.array([[10], [0]])
# In[12]:
vs
# In[13]:
isrc=irv.dot(vs)
# In[14]:
print(isrc)
# In[ ]:




