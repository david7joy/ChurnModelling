#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[81]:


url = 'https://community.watsonanalytics.com/wp-content/uploads/2015/03/WA_Fn-UseC_-Telco-Customer-Churn.csv?cm_mc_uid=51304980933215218170416&cm_mc_sid_50200000=92178841521817041648&cm_mc_sid_52640000=98592221521817041652'
data = pd.read_csv(url)


# In[82]:


print(f'Total Records in our Data :{data.shape[0]}')
print(f'Total Variables in our Data :{data.shape[1]}')
data.head(5).transpose()


# In[83]:


plt.hist(x=data['tenure'],bins=10,color='orange')
plt.xlabel('tenure')
plt.ylabel('records')
plt.title('Histogram of Tenure')
plt.show()


# Making dummy variables for churn variable !!

# In[84]:


data['churn_dummy'] = data.Churn.apply(lambda x: 1 if x=='Yes' else 0)


# In[85]:


data['MultipleLines'].value_counts()


# In[86]:


df = data[data.MultipleLines != 'No phone service']
df['Multiple_lines_dummy'] = df['MultipleLines'].apply(lambda x: 1 if x=='Yes' else 0)
df.Multiple_lines_dummy.value_counts()


# In[151]:


# Multiple Lines
kmf = KaplanMeierFitter()
T = list(df.tenure[df.Multiple_lines_dummy != 0]) 
C = list(df.churn_dummy[df.Multiple_lines_dummy != 0])
kmf.fit(T,C)
kmf.plot()


# In[163]:


# Multiple Lines
kmf1 = KaplanMeierFitter()
T1 = list(df.tenure[df.Multiple_lines_dummy != 1]) 
C1 = list(df.churn_dummy[df.Multiple_lines_dummy != 1])
kmf1.fit(T1,C1)
kmf1.plot()


# In[170]:


d1 = pd.DataFrame(data=kmf.survival_function_)
d2 = pd.DataFrame(data=kmf1.survival_function_)
d1['KMF1_SurvivalFunction'] = d2['KM_estimate']
d1.head(10)


# In[171]:


ax = plt.subplot(111)

kmf = KaplanMeierFitter()
for group in df['Multiple_lines_dummy'].unique():
    data1 = df[df.Multiple_lines_dummy != group]
    kmf.fit(data1.tenure, data1.churn_dummy, label=group)
    kmf.plot(ax=ax,figsize=(15,8))
    plt.xlabel('timeline',color='black')
    plt.ylabel('probability',color='black')
    plt.title('Kaplan Meier Curve for driver Multiple Lines 0:Yes 1:No')


# In[ ]:




