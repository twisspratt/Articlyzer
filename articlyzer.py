import json
import pandas as pd
import numpy as np
import requests
import string
from bs4 import BeautifulSoup
import datetime
from collections import Counter
import re 
import matplotlib.pyplot as plt
import nltk
from textblob import TextBlob
# This is the place where taking of json files 
# and putting all the words in their right places goes

# possible divisions of data:
#	by month or by day sequentially
# Tasks:
# 	count the words
#	histogram of each word? maybe words above a threshold?
#	make a word ven-diagram perhaps? common words? 
#	mentions of X -> make a funciton that takes in a word or phrase 
#	and spits out instances
#	title masher of the two -> requires grammer (how do that??)
#	title generator

# +++++
# Make an object with like word count, 
# unique etc as properties of the object???
# SET UP SERVER TO GET THIS DATA EVERY DAY
# INCORPORATE DATE INTO THINGS TO GET HISTORIC 
# AND OVER TIME AVERAGES ETC
# Attempts to get all the induvidual words
# then returns list of each word in file


# Required sprucing:
#	Are all the duplicates really gone?
#	needs a function to cut out words that don't matter:
#	such as the etc
#	need a thing to add together similar words maybe?
#	such as trump, trumpism etc
#	How should i display the data? there's too many words
#	maybe top 100 nouns? 
#	save the plots also with a datetime?
#	maybe make that like do it with the daily scraping?

def word_extractor(articles_from_site): 
	# might be easier to do nltk.word_tokenize(shit)
	# takes json file and returns a list of words 
	# with no special chars
	words = []
	word_list = []
	titles = []
	with open(articles_from_site) as file:
		raw_file = json.load(file)
		less_raw_file = raw_file['articles']
		for days in less_raw_file:
			titles.append(days['titles']) # article arrays
			for day_of_titles in titles:
				for title in day_of_titles:
						word_list.append(title.split())
		for title_chunk in word_list:
			for i in title_chunk:
				words.append(re.sub(r'\W+', '',i))
	return words

def word_counter(word_list): 
	#returns a dict that has a count of each word
	count = Counter(word_list)
	return dict(count)
	
def word_hist(word_count): 
	# gives diagnostics of given word_count
	# do we want an i/o where like you request a type of graph 
	# and it gives it 
	# to you and then asks if you want more and then gives quit option
	fig, ax = plt.subplots()
	new_count = {}
	for key in word_count:
		if word_count[key]<1000: new_count[key]=word_count[key]
	word = [keys for keys in new_count.keys()]
	count = [counts for counts in new_count.values()]
	ax.bar(word, count, color='salmon')
	ax.set_title('Shit')
	plt.xticks(rotation=90)
	plt.rc('font', size=8) 
	plt.show()

def part_of_speech(word_list):
	organized_speech_parts={}
	unique_words=[key for key in word_counter(word_list).keys()]
	for word in unique_words:
		blob=TextBlob(word)
		tags=blob.tags
		if tags[0][1] not in organized_speech_parts.keys():
			organized_speech_parts[tags[0][1]]=[str(tags[0][0])]
		else: organized_speech_parts[tags[0][1]].append(str(tags[0][0]))
	return organized_speech_parts


	# assigns a part of speech to each word in the list
	# using nltk and then returns a dict with a list of words 
	# of each speech type

# def word_venn(word_list1, word_list2):
# 	# returns interactive vendiagram of common words and
# 	# their relative stregths

# def remove_words(word_list):
# 	#removes common and uninteresting words

# def article_generator(hmm idk yet):

# # Grammer stuff?
# # Article Generatorrrrrrrrr fun 

# tokenized = sent_tokenize(txt) 
# for i in tokenized: 
      
#     # Word tokenizers is used to find the words  
#     # and punctuation in a string 
#     wordsList = nltk.word_tokenize(i) 
  
#     # removing stop words from wordList 
#     wordsList = [w for w in wordsList if not w in stop_words]  
  
#     #  Using a Tagger. Which is part-of-speech  
#     # tagger or POS-tagger.  
#     tagged = nltk.pos_tag(wordsList) 
  
#     print(tagged) 


























