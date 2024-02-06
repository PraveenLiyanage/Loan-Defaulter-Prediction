#!/usr/bin/env python
# coding: utf-8

# In[23]:


#Basic libraries
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#Model libraries
from sklearn.model_selection import train_test_split

import xgboost
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE

import pickle


# In[8]:


data = pd.read_csv('Cleaned_final_file.csv',index_col=0)
data.head()


# In[20]:


df_model = data[['Term','GrAppv','SBA_Appv','NoEmp','RetainedJob','CreateJob','RevLineCr_Y','MIS_Status']]

X = df_model.drop('MIS_Status',axis = 1)
y = df_model['MIS_Status']

x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=10)



# In[21]:


#Oversampling minority class

sm = SMOTE(random_state=42, sampling_strategy=1.0)

Xsmot_train, ysmot_train = sm.fit_resample(x_train,y_train)


# In[24]:


xb = XGBClassifier()
model = xb.fit(Xsmot_train,ysmot_train)


# In[25]:


pickle.dump(model, open("model.pkl", "wb"))


# In[ ]:




