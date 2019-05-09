import json
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import datetime
import time
## more ideas:

## obv make this a function with a website input
## create the larger program that spits out things about the site// collects info on it each day and then updates
## the content over time. 

url_one= 'https://slate.com/'
url_two = 'https://www.breitbart.com/'


####################################SLATE############################################
r=requests.get(url_one) 															# sends a get to Slate
slate_soup=BeautifulSoup(r.content, 'html.parser') 									# html parses the website with Bsoup4
articles_full_html=slate_soup.find_all('h3')	   									# slate's titles are tagged under h3
article_names=[str.strip(titles.get_text()) for titles in articles_full_html] 		# gets titles from h3 tag
article_names=list(set(article_names)) 												# Creates list of unique article names
article_date=str(datetime.datetime.now())											# Records the datetime of get
article_dict_entry = {"date": article_date, "titles": article_names} 				# Creates a JSON-able python dict
with open('slate_articles.json') as f: 												# you open the outdated json file, read it in as a dict
	articles = json.load(f)															# is this dangerous?
	articles['articles'].append(article_dict_entry) 							# then append the new titles to the dict inside python
	with open('slate_articles.json', 'w') as g: 									# then write over the old file! 
		json.dump(articles, g, ensure_ascii = False)


####################################BREITBART########################################
k=requests.get(url_two)
breit_soup=BeautifulSoup(k.content, 'html.parser')
b_articles_full_html=breit_soup.find_all('h2')
b_article_names=[str.strip(titles.get_text()) for titles in b_articles_full_html]
b_article_date=str(datetime.datetime.now())
b_article_names=list(set(b_article_names))
b_article_dict_entry = {"date": b_article_date, "titles": b_article_names}
with open('breitbart_articles.json') as f: 											# you open the outdated json file, read it in as a dict
	articles = json.load(f)															# is this dangerous?
	articles['articles'].append(b_article_dict_entry) 					# then append the new titles to the dict inside python
	with open('breitbart_articles.json', 'w') as g: 								# then write over the old file! 
		json.dump(articles, g, ensure_ascii = False)

 ####################################################################################
