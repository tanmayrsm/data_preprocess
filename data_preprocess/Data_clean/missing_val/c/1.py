import csv 
import pandas as pd
import numpy as np

data = pd.read_csv('Melbourne_housing_dataset_full.csv')

#get row no of missing values 
row_no = []

for index ,rows in data.iterrows():
	if('NaN' in str(rows)):
		row_no.append(index)


data = data.interpolate(method = 'linear' , limit_direction = 'backward')
data = data.fillna(method = 'pad')

print('reading done')

#get rows from interpolated df and write in csv
print(len(row_no))


for i in range(0,len(row_no)):
	new_data_frame = data.iloc[row_no[i],:]

	export_csv = new_data_frame.to_csv(r'D:\Tan\itb\ML_assn\data_preprocess\Data_clean\missing_val\c\extracted.csv' ,mode='a',index = None ,header = True)

# for l in row_no:
# 	print(data.iloc[l])





