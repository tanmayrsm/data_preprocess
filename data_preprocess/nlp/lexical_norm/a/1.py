import glob
import xml.etree.ElementTree as ET
import os
import re
import string
import itertools as it
from bs4 import BeautifulSoup

from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

ps = PorterStemmer() 

def freq(stringo):
	g = ''
	#break into words
	str_ka_list = stringo.split()

	x = set(str_ka_list)

	for words in x:
		g = g + '\n' + ' ' + words + ': ' + str(str_ka_list.count(words))
	return g

def operation(filename):
	btree = BeautifulSoup(open(filename), "lxml-xml")
	print('In file : \n' + filename)
	gio = open('stems.csv','a+')
	gio.write('\n In file:' + filename + '\n')
	posts = ''
	dum = '0'
	#punctuations = '''!()-[]{};:'"\\,<>.,./?@#$%^&*_~'''
	
	with open(filename,'r') as f:
	 for key,group in it.groupby(f,lambda line: line.startswith('tag')):
	    if not key:
	        group = list(group)
	        posttags = btree.find_all("post")
	
	        for text in posttags:
	        	#print(text.string)
	        	dum = str(int(dum)+1)
	        	posts = ""
	        	y = re.sub(r'[\n\t]*',"",text.string)
	        	y = y.replace(',',"")
	        	y = y.replace('.',"")
	        	worz = word_tokenize(y)

	        	for w in worz:
	        		gio.write(str(w)+":"+str(ps.stem(w)) + '\n')

	        	#print('post no:'+dum+'----------------------------------------------------')
	        	

	        	gio.write('post no:'+str(dum)+'----------------------------------------------------\n')
	        return
	    

filename = 'D:/Tan/itb/ML_assn/data_preprocess/nlp/blog_dataset/'

for filename in glob.glob(os.path.join(filename, '*.xml')):
	operation(filename)
	
