import glob
import xml.etree.ElementTree as ET
import os
from nltk.tokenize import sent_tokenize ,word_tokenize
import re
import string
import itertools as it
from bs4 import BeautifulSoup

import nltk.data ,codecs

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
	gio = open('frequency.csv','a+')
	gio.write('In file : ' + filename + '\n')
	posts = ''
	dum = '0'
	punctuations = '''!()-[]{};:'"\\,<>.,./?@#$%^&*_~'''
	
	with open(filename,'r') as f:
	 for key,group in it.groupby(f,lambda line: line.startswith('tag')):
	    if not key:
	        group = list(group)
	        posttags = btree.find_all("post")
	
	        for text in posttags:
	        	#print(text.string)
	        	gio.write('\n---------post no:' + dum)
	        	y = re.sub(r'[\n\t]*',"",text.string)
	        	y_sec = ""
	        	for char in y:
	        		if y not in punctuations:
	        			y_sec = y_sec + y
	        	n = freq(y)
	        	
	        	posts = posts + ':' + dum + '\n' + n
	        	posts  =posts.replace(',',"")
	        	gio.write(posts.replace('.',""))

	        	dum = str(int(dum)+1)

	# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

	# tokened_date = tokenizer.tokenize(date)
	# tokened_post = tokenizer.tokenize(post)

			
filename = 'D:/Tan/itb/ML_assn/data_preprocess/nlp/blog_dataset/'

for filename in glob.glob(os.path.join(filename, '*.xml')):
	operation(filename)
