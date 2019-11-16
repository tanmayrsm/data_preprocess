import pandas as pd
  
data = pd.read_csv("Melbourne_housing_dataset_full.csv")  
 
data = data.fillna(method = 'pad') 
data = data.fillna(data.mean())
#data = data['CouncilArea' , 'Regionname'].fillna(method = 'ffill' , inplace = True)
#data3 = data['Regionname'].fillna(method = 'ffill' , inplace = True)
export_csv = data.to_csv(r'D:\\Tan\\itb\\ML_assn\\Data_clean\\missing_val\\mmClean.csv' ,index = None ,header = True)
