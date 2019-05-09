import json
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import datetime
import time

# make it so news_scraper happens once a day or some shit
# 

start_date=datetime.datetime(2019, 4, 17, 10, 0, 0)
end_date=datetime.datetime(2019, 4, 22, 10, 0, 0)

while(datetime.datetime.now()<start_date):
	time.sleep(600)

while(datetime.datetime.now()>start_date and datetime.datetime.now()<end_date):
	Scrape_Sites()
	time.sleep(86400)