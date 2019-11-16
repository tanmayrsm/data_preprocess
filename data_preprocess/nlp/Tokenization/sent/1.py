import glob
import xml.etree.ElementTree as ET
import os
from nltk.tokenize import sent_tokenize
import re

import itertools as it
from bs4 import BeautifulSoup

import nltk.data ,codecs

def operation(filename):
	btree = BeautifulSoup(open(filename), "lxml-xml")

	date = ''
	post = ''
	dum = '0'
	with open(filename,'r') as f:
	 for key,group in it.groupby(f,lambda line: line.startswith('tag')):
	    if not key:
	        group = list(group)
	        datetags= btree.find_all("date")
	        posttags = btree.find_all("post")
	        for text in datetags:
	        	z = dum + '-' + text.string+'\n'
	        	#y = re.sub(r'[\n\t]*',"",y)
	        	dum = str(int(dum)+1)
	        	date += z

	        for text in posttags:
	        	y = re.sub(r'[\n\t]*',"",text.string)
	        	post += y + '\n'


	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

	tokened_date = tokenizer.tokenize(date)
	tokened_post = tokenizer.tokenize(post)


	with open('sentence.csv' ,'a+') as f1:
		for dates in tokened_date:
			f1.writelines(dates)
		for posts in tokened_post:
			f1.writelines('\n' + str(tokened_post.index(posts)) + '-' + posts)
	f1.close()

filename = 'D:/Tan/itb/ML_assn/data_preprocess/nlp/blog_dataset/'

for filename in glob.glob(os.path.join(filename, '*.xml')):
	operation(filename)
