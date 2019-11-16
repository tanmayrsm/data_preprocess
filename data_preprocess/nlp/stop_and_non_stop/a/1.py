import glob
import xml.etree.ElementTree as ET
import os
import re
import string
import itertools as it
from bs4 import BeautifulSoup


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

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
	#print('In file : \n' + filename)
	gio = open('stopwords.csv','a+')
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
	        	posts = ""
	        	y = re.sub(r'[\n\t]*',"",text.string)
	        	
	        	stop_wrds = set(stopwords.words('english'))
	        	wrd_tokens = word_tokenize(y)
	        	filter_sentence = [w for w in wrd_tokens if not w in stop_wrds]

	        	filtered_sent = []
	        	for w in wrd_tokens:
	        		if w in stop_wrds:filtered_sent.append(w)

	        	posts = posts + ':' + dum + '\n' + str(filtered_sent)
	        	
	        	dum = str(int(dum)+1)

	        	gio.write(posts)
	        return
	    
	gio.close()
filename = 'D:/Tan/itb/ML_assn/data_preprocess/nlp/blog_dataset/'

for filename in glob.glob(os.path.join(filename, '*.xml')):
	operation(filename)
	
