#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# # Loading Dataset

# In[6]:


df = pd.read_csv('hotel_booking.csv')


# # Exploratoary Data Analysis and Data Cleaning

# In[8]:


# dataframe sample
df.head()


# In[9]:


# number of rows and columns in dataframe
df.shape


# In[10]:


df.columns


# In[11]:


# datatype of every column
df.info()


# In[12]:


# converting object datatype to date datatype  
df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[13]:


df.describe(include = 'object')


# In[14]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[15]:


# null values
df.isnull().sum()


# In[16]:


df.drop(['company', 'agent'], axis = 1, inplace = True)


# In[17]:


# droping null values
df.dropna(inplace = True)


# In[18]:


df.describe()


# In[19]:


# ploting grap for Average Daily Rate 
df['adr'].plot(kind = 'box')


# In[20]:


# removing outlier
df = df[df['adr']<5000]


# # Data Analysis and Visualization

# In[21]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
print(cancelled_perc)


# In[46]:


plt.figure(figsize = (5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled', 'Canceled'], df['is_canceled'].value_counts(), edgecolor = 'k', width = 0.7)
plt.show()


# In[22]:


# reservation status in differennt hotel
plt.figure(figsize=(8,4))
ax1 = sns.countplot(data=df, x='hotel', hue='is_canceled', palette='Blues')
plt.title('Reservation status in differennt hotel', size =20)
plt.xlabel('Hotel')
plt.ylabel('number of reservations')
plt.legend(['not canceled', 'canceled'])
plt.show()


# In[23]:


resort_hotel = df[df['hotel']=="Resort Hotel"]
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[24]:


city_hotel = df[df['hotel']=="City Hotel"]
city_hotel['is_canceled'].value_counts(normalize=True)


# In[25]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[57]:


plt.figure(figsize=(20,8))
plt.title("Average Daily Rate in City and Resort Hotel", fontsize=30)
plt.plot(resort_hotel.index, resort_hotel['adr'], label='Resort Hotel')
plt.plot(city_hotel.index, city_hotel['adr'], label='City Hotel')
plt.legend(fontsize=20)
plt.show()


# In[27]:


df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='month', hue='is_canceled')
plt.title('Reservation Status per Month')
plt.xlabel('Month')
plt.ylabel('Count')
plt.legend(['not cancelled','cancelled'])
plt.show()


# In[28]:


# Calculate average daily rate (ADR) per month
adr_per_month = df[df['is_canceled']== 1].groupby('month')['adr'].sum().reset_index()

# Create a bar plot of ADR per month
plt.figure(figsize=(12, 6))
sns.barplot(data=adr_per_month, x='month', y='adr')
plt.title('Average Daily Rate (ADR) per Month')
plt.xlabel('Month')
plt.ylabel('ADR')
plt.show()


# In[30]:


cancelled_data =df[df['is_canceled']==1]
top_10_countries=cancelled_data['country'].value_counts()[:10]
plt.figure(figsize=(8, 8))
plt.title('Top 10 Countries with Reservation Cancelled')
plt.pie(top_10_countries, autopct='%.2f',labels=top_10_countries.index)
plt.show()


# In[31]:


df['market_segment'].value_counts(normalize=True)


# In[32]:


cancelled_data['market_segment'].value_counts(normalize=True)


# In[33]:


# Analyze cancellation rate by market segment
df_market_segment = cancelled_data['market_segment'].value_counts(normalize=True).mul(100)
plt.figure(figsize=(12, 6))
sns.barplot(x=df_market_segment.index,  y=df_market_segment.values)
plt.title('Cancellation Rate by Market Segment')
plt.xlabel('Market Segment')
plt.ylabel('Cancellation percent')
plt.xticks(rotation=90)
plt.show()


# In[34]:


cancelled_df_adr = cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace=True)
cancelled_df_adr.sort_values('reservation_status_date', inplace=True)

not_cancelled_data =df[df['is_canceled'] ==0]
not_cancelled_df_adr = not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace=True)
not_cancelled_df_adr.sort_values('reservation_status_date', inplace=True)

plt.figure(figsize=(20,8))
plt.title('Average Daily Rate', fontsize=25)
plt.plot(not_cancelled_df_adr['reservation_status_date'], not_cancelled_df_adr['adr'], label='not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'], cancelled_df_adr['adr'], label='cancelled')
plt.legend()


# In[35]:


cancelled_df_adr = cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016') & (cancelled_df_adr['reservation_status_date']<'2017-09')]
not_cancelled_df_adr = not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>'2016') & (not_cancelled_df_adr['reservation_status_date']<'2017-09')]


# In[36]:


plt.figure(figsize=(20,8))
plt.title('Average Daily Rate', fontsize=20)
plt.plot(not_cancelled_df_adr['reservation_status_date'], not_cancelled_df_adr['adr'], label='not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'], cancelled_df_adr['adr'], label='cancelled')
plt.legend(fontsize=20)
plt.show()


# In[ ]:




