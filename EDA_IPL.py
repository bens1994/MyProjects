#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importing required Libraries


# In[42]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# In[ ]:


#Loading the dataset


# In[2]:


Matches = pd.read_csv('matches[1].csv')


# In[ ]:


# Head() method is used to print first 5 records of the dataset


# In[3]:


Matches.head()


# In[ ]:


# Shape attribute is used to verify no. of rows and columns


# In[4]:


Matches.shape


# In[61]:


Matches['player_of_match'].value_counts()[0:5]


# In[12]:


import seaborn as sns


# In[63]:


plt.figure(figsize=(7,7))
plt.bar(list(Matches['player_of_match'].value_counts()[0:5].keys()),list(Matches['player_of_match'].value_counts()[0:5]),color=["blue","green","pink","brown","orange"])
plt.show()


# In[64]:


Matches['result'].value_counts()


# In[66]:


Matches['toss_winner'].value_counts()


# In[76]:


batting_first = Matches[Matches['win_by_runs']!=0]


# In[77]:


batting_first.head()


# In[80]:


plt.figure(figsize=(7,7))
plt.hist(batting_first['win_by_runs'])
plt.title("Graph")
plt.grid()
plt.show()


# In[100]:


batting_first['winner'].value_counts()[0:5]


# In[98]:


plt.figure(figsize=(15,7))
plt.bar(list(batting_first['winner'].value_counts()[0:5].keys()), list(batting_first['winner'].value_counts()[0:5]),color = ["pink","brown","red","blue","yellow"])
plt.show()


# In[111]:


plt.figure(figsize=(15,7))
plt.pie(list(batting_first['winner'].value_counts()), labels = list(batting_first['winner'].value_counts().keys()), autopct='%0.01f%%')
plt.show()


# In[116]:


batting_second = Matches[Matches['win_by_wickets']!=0]


# In[118]:


batting_second.head()


# In[121]:


plt.figure(figsize=(5,5))
plt.hist(batting_second['win_by_wickets'],bins=25)
plt.show()


# In[125]:


batting_second['winner'].value_counts()


# In[128]:


plt.figure(figsize=(15,5))
plt.bar(list(batting_second['winner'].value_counts()[0:7].keys()),list(batting_second['winner'].value_counts()[0:7]),color = ["red","yellow","blue","green","pink","black","orange"])
plt.show()


# In[131]:


plt.figure(figsize=(5,7))
plt.pie(list(batting_second['winner'].value_counts()), labels = list(batting_second['winner'].value_counts().keys()), autopct='%0.1f%%')
plt.show()


# In[132]:


Matches['season'].value_counts()


# In[133]:


Matches['city'].value_counts()


# In[135]:


np.sum(Matches['toss_winner'] == Matches['winner'])


# In[137]:


Matches.shape


# In[138]:


393/756


# In[ ]:




