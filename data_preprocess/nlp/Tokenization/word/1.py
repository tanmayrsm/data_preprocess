import glob
import xml.etree.ElementTree as ET
import os
from nltk.tokenize import sent_tokenize ,word_tokenize
import re

import itertools as it
from bs4 import BeautifulSoup

import nltk.data ,codecs

def operation(filename):
	btree = BeautifulSoup(open(filename), "lxml-xml")

	dates = ''
	posts = ''
	dum = '0'
	with open(filename,'r') as f:
	 for key,group in it.groupby(f,lambda line: line.startswith('tag')):
	    if not key:
	        group = list(group)
	        posttags = btree.find_all("post")
	        
	        for text in posttags:
	        	y = re.sub(r'[\n\t]*',"",text.string)
	        	posts += y + '\n'


	# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

	# tokened_date = tokenizer.tokenize(date)
	# tokened_post = tokenizer.tokenize(post)
	posts = word_tokenize(re.sub(r'[^\w\s]','',posts))
	#print(word_tokenize(posts))



	with open('word.csv' ,'a+') as f1:
		for post in posts:
			f1.writelines('\n' + str(posts.index(post)) + '-' + post)
	f1.close()

filename = 'D:/Tan/itb/ML_assn/data_preprocess/nlp/blog_dataset/'

for filename in glob.glob(os.path.join(filename, '*.xml')):
	operation(filename)
