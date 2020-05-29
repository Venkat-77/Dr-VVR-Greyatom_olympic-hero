# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Path of the file
path
data = pd.read_csv(path)
data = pd.DataFrame(data)
data.rename(columns = {'Total':'Total_Medals'}, inplace = True) 
data.head(10)


#Code starts here



# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Path of the file
path
data = pd.read_csv(path)
data = pd.DataFrame(data)
data['Better_Event'] = None
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'], 'Summer', 'Winter')
data['Better_Event'] =np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event'])
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Path of the file
path
set1 = []
set2 = []
set3 = []
s1 = []
common = []
data = pd.read_csv(path)
data = pd.DataFrame(data)
data.rename(columns = {'Total':'Total_Medals'}, inplace = True) 
top_countries = data.loc[:, ['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'] ]
print(top_countries.head())
top_countries.drop(top_countries.tail(1).index,inplace=True)
def top_ten(df,col):
    country_list = []
    top_10=df.nlargest(10, col)
    #print(top_10)
    print("="*50)
    country_list = top_10['Country_Name'].values.tolist()
    return country_list  
top_10_summer = top_ten(top_countries,"Total_Summer")    
top_10_winter = top_ten(top_countries,"Total_Winter")    
top_10 = top_ten(top_countries,"Total_Medals")     
set1 = set(top_10_summer)
set2 = set(top_10_winter)
set3 = set(top_10)
s1 = set1.intersection(set2)
common = list(s1.intersection(set3))
print(common)



# --------------
#Code starts here
import matplotlib.pyplot 
path
set1 = []
set2 = []
set3 = []
s1 = []
common = []
data = pd.read_csv(path)
data = pd.DataFrame(data)
data.rename(columns = {'Total':'Total_Medals'}, inplace = True) 
top_countries = data.loc[:, ['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'] ]
print(top_countries.head())
top_countries.drop(top_countries.tail(1).index,inplace=True)
def top_ten(df,col):
    country_list = []
    top_10=df.nlargest(10, col)
    #print(top_10)
    print("="*50)
    country_list = top_10['Country_Name'].values.tolist()
    return country_list  
top_10_summer = top_ten(top_countries,"Total_Summer")    
top_10_winter = top_ten(top_countries,"Total_Winter")    
top_10 = top_ten(top_countries,"Total_Medals")     
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
plt.figure(figsize=[14,8])
plt.xlabel("Country_Summer")
plt.ylabel("No of Medals")
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.show()
plt.figure(figsize=[14,8])
plt.xlabel("Country_Winter")
plt.ylabel("No of Medals")
plt.bar(summer_df['Country_Name'],winter_df['Total_Winter'])
plt.show()
plt.figure(figsize=[14,8])
plt.xlabel("Country_Summer")
plt.ylabel("No of Medals")
plt.bar(summer_df['Country_Name'],top_df['Total_Medals'])
plt.show()









# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Path of the file
path
data = pd.read_csv(path)
data = pd.DataFrame(data)
data.rename(columns = {'Total':'Total_Medals'}, inplace = True) 
top_countries = data.loc[:, ['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'] ]
top_countries.drop(top_countries.tail(1).index,inplace=True)
def top_ten(df,col):
    country_list = []
    top_10=df.nlargest(10, col)
    #print(top_10)
    print("="*50)
    country_list = top_10['Country_Name'].values.tolist()
    return country_list  
top_10_summer = top_ten(top_countries,"Total_Summer")    
top_10_winter = top_ten(top_countries,"Total_Winter")    
top_10 = top_ten(top_countries,"Total_Medals")     
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
print(summer_df.head())
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer'] 
summer_max_ratio=max(summer_df['Golden_Ratio']) 
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter'] 
winter_max_ratio=max(winter_df['Golden_Ratio']) 
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals'] 
top_max_ratio=max(top_df['Golden_Ratio']) 
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print("="*50)
print(summer_max_ratio)
print(summer_country_gold)
print("="*50)
print(winter_max_ratio)
print(winter_country_gold)
print("="*50)
print(top_max_ratio)
print(top_country_gold)


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Path of the file
path
data = pd.read_csv(path)
data = pd.DataFrame(data)
data.rename(columns = {'Total':'Total_Medals'}, inplace = True) 
data_1 = data.drop(data.tail(1).index)
data_1 = pd.DataFrame(data_1)
print(data_1.head())
data_1['Total_Points'] = 3*data_1['Gold_Total'] + 2*data_1['Silver_Total'] + data_1['Bronze_Total']
most_points = max(data_1['Total_Points']) 
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points)
print(best_country)




# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Path of the file
path
data = pd.read_csv(path)
data = pd.DataFrame(data)
data.rename(columns = {'Total':'Total_Medals'}, inplace = True) 
best_country = "United States"
best = data.loc[data['Country_Name']=="United States",:]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)
best.plot.bar()
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)
plt.show()


