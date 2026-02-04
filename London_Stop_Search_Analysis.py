#!/usr/bin/env python
# coding: utf-8

# apa: Romina Barzamini, Suraj Ajit (2026). Raw and Processed Stop-and-Search Dataset for London (2022–2024). IEEE Dataport. https://dx.doi.org/10.21227/x645-5z64 

# In[28]:


import math
import datetime
import numpy as np
import pandas as pd
import matplotlib


# In[21]:


stopSearchMay2022 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202205.csv")
stopSearchJune2022 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202206.csv")
stopSearchJuly2022 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202207.csv")
stopSearchAugust2022 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202208.csv")
stopSearchSeptember2022 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202209.csv")
stopSearchOctober2022 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202210.csv")
stopSearchNovember2022 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202211.csv")
stopSearchDecember2022 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202212.csv")
stopSearchJanuary2023 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202301.csv")
stopSearchFebruary2023 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202302.csv")
stopSearchMarch2023 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202303.csv")
stopSearchApril2023 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202304.csv")
stopSearchMay2023 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202305.csv")
stopSearchJune2023 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202306.csv")
stopSearchJuly2023 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202307.csv")
stopSearchAugust2023 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202308.csv")
stopSearchSeptember2023 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202309.csv")
stopSearchOctober2023 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202310.csv")
stopSearchNovember2023 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202311.csv")
stopSearchDecember2023 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202312.csv")
stopSearchJanuary2024 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202401.csv")
stopSearchFebruary2024 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202402.csv")
stopSearchMarch2024 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202403.csv")
stopSearchApril2024 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202404.csv")
stopSearchMay2024 = pd.read_csv("/Users/katiemeadows/Downloads/stop_and_search_dataport/raw_data/202405.csv")
allDataList =[stopSearchMay2022, stopSearchJune2022, stopSearchJuly2022, stopSearchAugust2022, stopSearchSeptember2022, stopSearchOctober2022, 
              stopSearchNovember2022, stopSearchDecember2022, stopSearchJanuary2023, stopSearchFebruary2023, stopSearchMarch2023, stopSearchApril2023,
              stopSearchMay2023, stopSearchJune2023, stopSearchJuly2023, stopSearchAugust2023, stopSearchSeptember2023, stopSearchOctober2023,
              stopSearchNovember2023, stopSearchDecember2023, stopSearchJanuary2024, stopSearchFebruary2024, stopSearchMarch2024, stopSearchApril2024,
              stopSearchMay2024
             ]


# In[56]:


stopSearchApril2023.head(25)


# In[38]:


for i in range(len(allDataList)):
    Type=allDataList[i]['Type']
    Date=allDataList[i]['Date']
    operationBool=allDataList[i]['Part of a policing operation']
    Gender=allDataList[i]['Gender']
    ageRange=allDataList[i]['Age range']
    ethnicitySelfReport=allDataList[i]['Self-defined ethnicity']
    ethnicityOfficerReport=allDataList[i]['Officer-defined ethnicity']
    objectSearch=allDataList[i]['Object of search']
    Outcome=allDataList[i]['Outcome']


# In[89]:


ethnicityMisreport=[]
for i in range(len(allDataList)):
    if ethnicityOfficerReport[i]!=ethnicitySelfReport[i]:
        ethnicityMisreport.append(allDataList[i])
ethnicityMisReport_Black=0
ethnicityMisReport
for i in range(len(ethnicityMisreport)):
    if ethnicityOfficerReport=='Black' and (ethnicitySelfReport!='Black/African/Caribbean/Black British - Any other Black/African/Caribbean background' or ethnicitySelfReport!='Black/African/Caribbean/Black British - Black' or ethnicitySelfReport!='Black/African/Caribbean/Black British - African' or ethnicitySelfReport!='Black/African/Caribbean/Black British - Caribbean' or ethnicitySelfReport!='Black/African/Caribbean/Black British - Black British'):
        print()
    
        


# In[90]:


print(ethnicityMisreport)


# In[ ]:




