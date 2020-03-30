#!/usr/bin/env python
# coding: utf-8

# In[4]:


#HOMEWORK 1:Web Site inputs


# In[2]:


import bs4
import pandas as pd
import requests


# In[3]:


response = requests.get('https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db')
print(response.text) # Print the output


# In[6]:


soup = bs4.BeautifulSoup(response.text, "html.parser")
print(soup.prettify()) # Print the output using the 'prettify' function cleaner


# In[7]:


# Access the title element
soup.title


# In[8]:


# Access the content of the title element
soup.title.string


# In[9]:


# Access data in the first 'p' tag
soup.div


# In[14]:


data = soup.findAll(attrs={'class':'DataTable_Cell-sc-1d2l9ix DataTable_TableCell-sc-13l0208 loOctw'}#calısmyoooor
for i in data:
    print(i.string)


# In[1]:


print #####cvs import


# In[27]:


f = open('SpotifyFeatures.csv','a') # open new file, make sure path to your data file is correct

p = 0 # initial place in array
l = len(data)-1 # length of array minus one


f.write("County, State, FIPS Code, Total Pop, Median Income ($), No. of Housing Units, Median Home Value ($), No. of Owner Occupied Housing Units, No. of Owner Occ. Housing Units with Debt, No. of Owner Occ. Housing Units without Debt\n") #write headers


while p < l: # while place is less than length
    f.write(data[p].string + ", ") # write county and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write FIPS and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write Total Pop and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write Median Income and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write No. of Housing Units and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write Median Home Value and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write No. of Owner Occupied Housing Units and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write No. of Owner Occ. Housing Units with Debt and add comma
    p = p + 1 # increment
    f.write(data[p].string + "\n") # write No. of Owner Occ. Housing Units without Debt and line break
    p = p + 1 # increment

    
f.close() # close file


# In[18]:


spoti = pd.read_csv('SpotifyFeatures.csv')


# In[19]:


spoti.shape


# In[20]:


spoti


# In[ ]:





# In[23]:


from sklearn import linear_model
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.model_selection import train_test_split


# In[24]:


corrMatrix = spoti.corr()
sn.heatmap(corrMatrix, annot=True)


# In[30]:


spoti.plot(x='popularity', y='danceability', style='o')  
plt.title('popularity vs danceability')  
plt.xlabel('popularity')  
plt.ylabel('danceability')  
plt.show()


# In[ ]:




