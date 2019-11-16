import pandas as pd

data = pd.read_csv('Melbourne_housing_dataset_full.csv')

# data.head()
ele = data.dropna(axis = 'columns')	#drop column with na values

export_csv = ele.to_csv(r'D:\\Tan\\itb\\ML_assn\\Data_clean\\drop_columns\\res.csv' ,index = None ,header = True)

print('column with no null values done in res.csv')