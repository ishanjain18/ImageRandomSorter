#!/usr/bin/env python
# coding: utf-8

# In[30]:


# This sorter sorts Images by Renaming Images Randomly, so you will lose your Image Names, be careful
# Its always better to work on a copy
import random
import os


# In[31]:


#Enter path to FOLDER Containing the Images, do not replace the r outside the double quotes

path = r"Enter folder path here"


# In[33]:


# Run this cell only ONCE to finish task.

images = os.listdir(path)
numlist = [i for i in range(len(images))]

for i in range(len(numlist)):
    num = random.choice(numlist)
    read_path = os.path.join(path, images[i])
    write_path = os.path.join(path, str(num) + images[i])
    os.rename(read_path,write_path)
    numlist.remove(num)

