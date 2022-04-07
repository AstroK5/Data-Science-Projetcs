#!/usr/bin/env python
# coding: utf-8

# # US EXPLORATORY DATA ANALYSIS

# In[48]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset.

# In[2]:


df = pd.read_csv("/Users/karnikabhardwaj/Downloads/US_Accidents_Dec21_updated.csv")
df.head()


# In[3]:


# check for null values

pd.isnull(df).sum()


# In[4]:


# get the information about the dataset

df.info()


# In[6]:


# get the statistical data of the dataset

df.describe().transpose()


# Query :Remove the columns we don't want (The most null values)

# In[7]:


df.columns


# In[10]:


# Top 20 Cities by accident

cities_by_accident = df.City.value_counts()
cities_by_accident.head(20)


# In[15]:


# plot the graph of the top 20 cities

cities_by_accident[:20].plot(kind='bar').set(title="Number of accidents vs Cities ")


# In[28]:


# Distribution between accidents

sns.set_style("darkgrid")
sns.distplot(cities_by_accident).set(title="Density of Accidents")


#  Most cities have less than 2000 accidents. 
#  Number of accident per city decreases/increases exponentially.

# In[22]:


list(cities_by_accident)
high_accident_cities = cities_by_accident[cities_by_accident>=1000]
low_accident_cities = cities_by_accident[cities_by_accident<1000]


# In[23]:


# Number of cities with accidents greater than 1000

len(high_accident_cities)


# In[24]:


# Number of cities with accidents less than 1000

len(low_accident_cities)


# In[25]:


len(high_accident_cities)/len(low_accident_cities)


#  Less than 5 % cities have less than 1000 accidents.

# In[32]:


# Analysis using Time

df.Start_Time


# In[33]:


# convert Start_Time into DATE type


# In[34]:


df.Start_Time = pd.to_datetime(df.Start_Time)


# In[35]:


df.Start_Time[0]


# In[40]:


# Accidents with respect to Day of the week
sns.distplot(df.Start_Time.dt.hour, bins=24, kde=False, norm_hist=True).set(title="Number of accident vs Time(Hours)")


# Most accidents happens during 7pm-9pm.

# In[43]:


# Accidents with respect to Day of the week

sns.distplot(df.Start_Time.dt.dayofweek, bins=7, kde=False, norm_hist=True).set(title="Number of accident vs Day")


#  Saturday and Sunday have the least accidents.

# In[45]:


# Accidents with respect to Month in an year



sns.distplot(df.Start_Time.dt.month, bins=12, kde=False, norm_hist=True).set(title="Number of accident vs Month")


#  More accidents are in winters.
