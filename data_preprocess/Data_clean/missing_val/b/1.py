import pandas as pd

data = pd.read_csv('Melbourne_housing_dataset_full.csv')

#data = data.fillna(data.mean())
data = data.interpolate(method = 'linear' ,limit_direction = 'backward')
data = data.fillna(method = 'pad')


export_csv = data.to_csv(r'D:\\Tan\\itb\\ML_assn\\Data_clean\\missing_val\\b\\LiClean.csv' ,index = None ,header = True)