import json
import pandas as pd
import numpy as np
import requests
import string
from bs4 import BeautifulSoup
import datetime
from collections import Counter
import re 

# This is the place where taking of json files and putting all the words in their right places goes
# possible divisions of data:
#	by month or by day sequentially
# Tasks:
# 	count the words
#	histogram of each word? maybe words above a threshold?
#	make a word ven-diagram perhaps? common words? 
#	mentions of X -> make a funciton that takes in a word or phrase and spits out instances
#	title masher of the two -> requires grammer (how do that??)
#	title generator

# +++++
# Make an object with like word count, unique etc as properties of the object???
# SET UP SERVER TO GET THIS DATA EVERY DAY
# INCORPORATE DATE INTO THINGS TO GET HISTORIC AND OVER TIME AVERAGES ETC

with open('slate_articles.json') as f:
	raw_slate = json.load(f)


# Attempts to get all the induvidual words
# then returns list of each word in file

def word_extractor(f):
	words = []
	word_list = []
	titles = []
	with open(f) as outfile:
		raw_file = json.load(outfile)
		less_raw_file = raw_file['articles']
		for days in less_raw_file:
			titles.append(days['titles']) # this is just the article arrays
			for day_of_titles in titles:
				for title in day_of_titles:
						word_list.append(title.split())
		for title_chunk in word_list:
			for i in title_chunk:
				words.append(i)
	return words

def word_counter(word_list):
	count = Counter(word_list)
	return count
	
# Grammer stuff?

# Article Generatorrrrrrrrr fun 





word_count = {}

