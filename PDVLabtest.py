
# coding: utf-8

# In[3]:

import pandas as pd
from pandas import DataFrame
import numpy as np
df=pd.read_csv('Accident_Cities.csv')
df.head()


# In[5]:

df1=pd.read_csv('Accident_States.csv')
df1.head()


# In[16]:

a=df['Persons Killed - 2011'].sum()
a


# In[17]:

b=df['Persons Injured - 2012'].sum()
b


# In[25]:

#1
df[df['Persons Killed - 2011']==df['Persons Killed - 2011'].max()][['Name of City']].head(3)


# In[27]:

df[df['Persons Injured - 2011']==df['Persons Injured - 2011'].max()][['Name of City']]


# In[28]:

df[df['Persons Injured - 2012']==df['Persons Injured - 2012'].max()][['Name of City']]


# In[92]:

df[df['Fatal Accidents - 2013']==df['Fatal Accidents - 2013'].max()]['Name of City']


# In[36]:

df[df['Injured - 2014']==df['Injured - 2014'].max()]['Name of City']


# In[37]:

df[df['Injured - 2015']==df['Injured - 2015'].max()]['Name of City']


# In[40]:

year=df['Persons Injured - 2011'].count()
year


# In[41]:

year1=df['Persons Injured - 2012'].count()
year1


# In[46]:

df[df['Persons Injured - 2011']==df['Persons Injured - 2011'].min()]['Name of City']


# In[47]:

df[df['Persons Injured - 2012']==df['Persons Injured - 2012'].min()]['Name of City']


# In[99]:

df1.sort_values('Unnamed: 1',ascending=False)['Unnamed: 0'].head(3)


# In[96]:

#2
df1.sort_values('KIlled due to Over Speed',ascending=False)['Unnamed: 0'].head(5)


# In[97]:

import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.pyplot import rc
x=[15,1,24,12,22]
x_pts=np.arange(len(x))
plt.plot(x,x_pts,marker='*',label='Name of cities')
plt.xlabel("No of people")
plt.legend()
plt.ylabel("Cities")
plt.tight_layout()
plt.show()


# In[68]:

#3
df1['KIlled due to Over Speed'].mean()


# In[79]:

#4
maximumdeath=df[['Persons Killed - 2011','Persons Killed - 2012','Fatal Accidents - 2013','Severity - 2014','Killed - 2015']].max()
maximumdeath


# In[84]:

#5
df[df['Persons Killed - 2011']==df['Persons Killed - 2011'].max()]['Name of City']


# In[85]:

df[df['Persons Killed - 2012']==df['Persons Killed - 2012'].max()]['Name of City']


# In[86]:

df[df['Fatal Accidents - 2013']==df['Fatal Accidents - 2013'].max()]['Name of City']


# In[87]:

df[df['Severity - 2014']==df['Severity - 2014'].max()]['Name of City']


# In[88]:

df[df['Killed - 2015']==df['Killed - 2015'].max()]['Name of City']


# In[90]:

import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.pyplot import rc
x=[7,7,7,24,7]
x_pts=np.arange(len(x))
name=['Delhi','Delhi','Delhi','Ludhiana','Delhi']
plt.plot(x,x_pts,marker='*',label='Name of cities')
plt.xlabel("No of people")
plt.legend()
plt.ylabel("Cities")
plt.tight_layout()
plt.show()


# In[95]:

#6
df1[['Accidents due to Alcohal and drugs','Unnamed: 0']]


# In[98]:

#7
df1[df1['Accidents due to Alcohal and drugs']==df1['Accidents due to Alcohal and drugs'].min()]['Unnamed: 0']


# In[ ]:



