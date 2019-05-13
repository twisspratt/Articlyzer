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
# Attempts to get all the induvidual words
# then returns list of each word in file


############ NEED TO TAKE OUT ', AND COUNTING DUPLICATES//WHY ARE THERED DUPES'
###MAYBE JUST WRITE A COUNTER UR SELF GOD DAMNIT

def word_extractor(articles_from_site): #takes json file and returns a list of unique words (no spec)
	words = []
	word_list = []
	titles = []
	with open(articles_from_site) as file:
		raw_file = json.load(file)
		less_raw_file = raw_file['articles']
		for days in less_raw_file:
			titles.append(days['titles']) # this is just the article arrays
			for day_of_titles in titles:
				for title in day_of_titles:
						word_list.append(title.split())
		for title_chunk in word_list:
			for i in title_chunk:
				words.append(re.sub(r'\W+', '',i))
	return words

def word_counter(word_list): #returns a dict that has a count of each word
	count = Counter(word_list)
	return dict(count)
	
def summary_stats(word_count): 
# gives diagnostics of given word_count
# do we want an i/o where like you request a type of graph and it gives it 
# to you and then asks if you want more and then gives quit option
	


	#def cmc_histo(card_list):
 #    fig, ax = plt.subplots()
 #    cost=[]
 #    count=[]
 #    histo_tuples= cmc_counter(card_list)
 #    for cmc_tuple in histo_tuples:
 #        cost.append(cmc_tuple[0])
 #        count.append(cmc_tuple[1])
 #    ax.bar(cost, count, color='salmon')
 #    ax.set_title('Count of Converted Mana Cost')
 #    ax.set_xlabel('Mana Costs')
 #    ax.set_ylabel('Count')
 #    plt.show()
#def article_generator(hmm idk yet):

# Grammer stuff?

# Article Generatorrrrrrrrr fun 



























