#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as mpb
import os
import re
import seaborn as sea


# In[8]:


os.path.isfile(r'C:\Users\48730\Downloads\AirBnb_data\Airbnb_Open_Data.csv')


# In[9]:


original = pd.read_csv(r'C:\Users\48730\Downloads\AirBnb_data\Airbnb_Open_Data.csv')


# In[10]:


air = original.copy()


# In[11]:


#Inspection starts..........


# In[12]:


air.info()


# In[19]:


air.shape


# In[21]:


air.describe()


# In[22]:


air['license'].unique()


# In[25]:


air['neighbourhood'].head(20)


# In[27]:


air['host_identity_verified'].info()


# In[29]:


air.iloc[10000]


# In[54]:


air[air['NAME'].str.contains(r'\d',na=False)].tail(20)


# In[ ]:


#Cleaning started///////////////////


# In[56]:


air.drop(columns=['house_rules','license'],inplace=True)


# In[58]:


air.drop(columns='country code',inplace=True)


# In[60]:


air.drop(columns='country',inplace=True)


# In[62]:


air.drop(columns='reviews per month',inplace=True)


# In[64]:


air.columns=air.columns.str.strip().str.capitalize().str.replace(r' ','_')


# In[66]:


air.rename(columns={'Lat':'Lattitude'},inplace=True)
air.rename(columns={'Long':'Longitude'},inplace=True)


# In[68]:


air['Construction_year']=pd.to_datetime(air['Construction_year'],errors='coerce')
air['Last_review']=pd.to_datetime(air['Last_review'],errors='coerce')


# In[70]:


#Cleaning values started////////


# In[130]:


air['Price']=air['Price'].replace(r'\,','',regex=True).fillna(0).astype(int)


# In[128]:


air['Service_fee']=air['Service_fee'].str.strip().fillna(0).astype(int)


# In[ ]:


air['Calculated_host_listings_count']=air['Calculated_host_listings_count'].fillna(0).astype(int)


# In[ ]:


cols=['Number_of_reviews','Minimum_nights']
air[cols]=air[cols].apply(lambda col: col.fillna(0).astype(int))


# In[85]:


air['Review_rate_number']=air['Review_rate_number'].fillna(0).astype(int)


# In[87]:


air['Service_fee']=air['Service_fee'].fillna(0)
air['Last_review']=air['Last_review'].fillna(0)
air['Lattitude']=air['Lattitude'].fillna(0)
air['Longitude']=air['Longitude'].fillna(0)
cols=['Host_name','Neighbourhood_group','Neighbourhood','Instant_bookable','Cancellation_policy']
for col in cols:
    air[col]=air[col].fillna('Unknown').str.strip()


# In[88]:


air['Cancellation_policy'].isna().value_counts()


# In[89]:


#Cleaning all extra signs,imoji,spaces betw words "Name" and Servise_fee columns


# In[93]:


air['Name']=air['Name'].str.replace(r'\s{2,}',' ',regex=True).str.strip()


# In[94]:


air['Name']=air['Name'].replace(r'\s+([/,.!?\+\-\(\)])',r'\1',regex=True)


# In[95]:


air['Name']=air['Name'].replace(r'([/,.!?\+\-\(\)])\s+',r'\1',regex=True)


# In[97]:


air['Name']=air['Name'].replace(r'(\w)\.+',r'\1.',regex=True)


# In[118]:


emoji_p = re.compile(
"["
"\U0001F600-\U0001F64F"
"\U0001F300-\U0001F5FF"
"\U0001F680-\U0001F6FF"
"\U0001F1E0-\U0001F1FF"
"\u2600-\u26FF"
"\u2700-\u27BF"
    "]+", flags=re.UNICODE)

air['Name']=air['Name'].str.replace(emoji_p,'',regex=True).str.strip()


# In[ ]:


air['Name']=air['Name'].replace(r'•+',r'',regex=True).str.strip()


# In[ ]:


air['Name']=air['Name'].str.capitalize()


# In[126]:


air['Service_fee']=air['Service_fee'].str.replace(r'\$','',regex=True).str.strip()
air['Price']=air['Price'].str.replace(r'\$','',regex=True).str.strip()


# In[ ]:


# filling Host_id_verif colmn with unkown using 3 cols.


# In[104]:


air['Host_identity_verified'] = air['Host_identity_verified'].fillna('unknown')


# In[106]:


air.info()


# In[134]:


air.info()


# In[138]:


top5 = air.groupby('Neighbourhood')['Price'].mean().sort_values(ascending=False).head(5)

sea.barplot(x=top5.index, y=top5.values)
sea.set_theme(font_scale=0.4)



# In[140]:


air.to_csv('Cleaned_airbnb',index=False)


# In[141]:


os.getcwd()


# In[142]:


folder='C:\\Users\\48730'


# In[143]:


folder


# In[ ]:




