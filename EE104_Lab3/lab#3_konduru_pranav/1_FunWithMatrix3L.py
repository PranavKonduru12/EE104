#!/usr/bin/env python
# coding: utf-8

# In[1]:
import numpy as np
# In[5]:
rv=np.array([ [20,-15,0,0],[-15,25,0,0],[-25,0,45,0],[-25,0,0,55]]) # 4x4 matrix because 4 loops
# In[6]:
rv
# In[7]:
irv=np.linalg.inv(rv)
# In[8]:
irv
# In[11]:
vs=np.array([[10],[-5],[0],[0]])
# In[12]:
vs
# In[13]:
isrc=irv.dot(vs)
# In[14]:
print(isrc)
# In[ ]:




