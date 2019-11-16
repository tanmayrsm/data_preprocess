import numpy as numpy
import pandas as pd
from sklearn.preprocessing import LabelEncoder

import category_encoders as ce

def get_index(data ,col_name):
	i = 0
	for col_name2 ,col_data in data.iteritems():
		if( col_name2 == col_name ):
			return i
		i += 1


le = LabelEncoder()

# read the data 
data = pd.read_csv('Melbourne_housing_dataset_full.csv')
data2 = pd.read_csv('Melbourne_housing_dataset_full.csv')

obj_dt = data.select_dtypes(include = ['object']).copy()

#specifying columns
encoder = ce.backward_difference.BackwardDifferenceEncoder(cols = ['CouncilArea'])
#obj_dt = data
encoder.fit(obj_dt ,verbose = 1)
l = encoder.transform(obj_dt).iloc[:,16:20]
#print(l)

g = data2.replace(to_replace = 'CouncilArea' ,value = 'l')
data2['CouncilArea'] = l['CouncilArea_12'].values


#specifying columns
encoder = ce.backward_difference.BackwardDifferenceEncoder(cols = ['Regionname'])
#obj_dt = data
encoder.fit(obj_dt ,verbose = 1)
l = encoder.transform(obj_dt).iloc[:,0:9]
#print(l)

g = data2.replace(to_replace = 'Regionname' ,value = 'l')
data2['Regionname'] = l['Regionname_0'].values



export_csv = data2.to_csv(r'D:\\Tan\\itb\\ML_assn\\categorical_encoding\\encoded.csv' ,index = None ,header = True)
# X = data.iloc[:,16].values	#fetch all rows and go till last column
# X = X.apply(lambda col: le.fit_transform(col))
# print(X)

# print(X)
# X = labelencoder_x.fit_transform(X)
# print(X)

