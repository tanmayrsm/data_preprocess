import pandas as pd
import numpy as np
import csv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from sklearn import ensemble
clf = ensemble.GradientBoostingRegressor(n_estimators = 400, max_depth = 5, min_samples_split = 2,
          learning_rate = 0.1, loss = 'ls')


df = pd.read_csv('LiClean.csv')

X = df[['Distance' ,'Postcode' ,'Bedroom2','Bathroom','Landsize' ,'BuildingArea' ,'YearBuilt','Lattitude','Longtitude']]
Y = df['Price']


X_train ,X_test ,y_train ,y_test = train_test_split(X,Y,test_size = 0.01)

print('X train size:',len(X_train))
print('X test size:',len(X_test))

#clf = LinearRegression()

clf.fit(X_train ,y_train)

#print(clf.predict(X_test) ,'\\\\n y test:' ,y_test)
print(clf.score(X_test ,y_test))

export_csv = y_test.to_csv(r'D:\\Tan\\itb\\ML_assn\\Building model\\predict_3.csv' ,mode='a',index = None ,header = True)


# with open('predict_1.csv', 'w') as csvfile: 
#     # creating a csv writer object 
#     csvwriter = csv.writer(csvfile) 
      
#     # writing the fields 
#     #csvwriter.writerow(fields) 
      
#     # writing the data rows 
#     csvwriter.writerows(g)
# with open('predict_1.csv', 'w') as writeFile:
# 	writer = csv.writer(writeFile)
# 	for line in g:
# 		print(line)
		# writer.writerow(line)
		# writer.writerow('\\n')

#export_csv = (X_test,y_test).to_csv(r'D:\\\\Tan\\\\itb\\\\ML_assn\\\\Building model\\\\predict_1.csv' ,index = None ,header = True)