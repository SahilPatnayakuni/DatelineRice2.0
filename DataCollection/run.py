from bs4 import BeautifulSoup
from newspaper import Article
import requests, sys, webhoseio

import metadata_extraction.metadata_extraction
import deduping.deduping
import collecting-data.pull_search

current_batch_objs = list()

def pull_from_search():
	webhose_newsriver_urls = set()

	response = requests.get("https://api.newsriver.io/v2/search?query=text%3A%22rice%20university%22%20OR%20title%3A%22rice%20university%22&sortBy=discoverDate&sortOrder=DESC&limit=15", headers={"Authorization":"sBBqsGXiYgF0Db5OV5tAw-SV99gJE88m8wacCchf2-RRrEiOATHNTquKXyn2goTIn2pHZrSf1gT2PUujH1YaQA"})
	jsonFile = response.json()
	all_newsriver_urls = set()

	for resp in jsonFile:
	    webhose_newsriver_urls.add(resp['url'])

	# webhoseio.config(token="25ad10f0-486b-408b-a8d2-0709e56808ce")
	# query_params = {
	#     "q": "\"rice university\"",
	#     "ts": "1536006194344",
	#     "sort": "published"
	# }

	# output = webhoseio.query("filterWebContent", query_params)
	# total_results = output['totalResults']
	# counter = int(1 + total_results / 100)

	# for i in range(counter):
	#     for j in range(100):
	#         try:
	#             url = output['posts'][j]['thread']['url']
	#             webhose_newsriver_urls.add(url)

	#             try:
	#                 author = output['posts'][i]['thread']['author']
	#             except Exception as e:
	#                 author = None

	#             published = output['posts'][i]['thread']['published']
	#             title = output['posts'][i]['thread']['title']

	#         except Exception as e:
	#             break
	#     output = webhoseio.get_next()
		
	for link in webhose_newsriver_urls:
		source = requests.get(link, timeout=5)
		BS = BeautifulSoup(source.content, "html.parser")
		print("LINK: " + link + "\n")
		print('\tURL: ' + source.url + "\n")
		
		try:
			print ('\t' + BS.find('title').text + "\n")
		except Exception as e:
			print("Could not find title")

		article = Article(source.url)
		article.download()

		if len(sys.argv) > 1 and sys.argv[1] == "--content":
			print(article.text)

		article.parse()
		print("\tAUTHORS: " + str(article.authors) + "\n")
		print("\tPUBLISH DATE: " + str(article.publish_date) + "\n")
		article.nlp()
		print("\tKEYWORDS: " + str(article.keywords) + "\n")
		print("\tSUMMARY: " + str(article.summary) + "\n")

def pull_from_feeds():
	pass

def extract_metadata(url, articleData):
	me = MetadataExtractor(url, articleData)
	me.extract_missing()
	
	return me.article_data

def is_uniq_article(obj):
	pass

def is_valid_article(obj):
	return True

def lookup_person():
	pass

def send_data():
	pass

if __name__ == "__main__":
	search_articles = pull_from_search()
	feed_articles= pull_from_feeds()

	all_articles = [search_articles, feed_articles]
	extracted_data = []

	for article in all_articles:

		extracted_data.append(extract_metadata(article.url, article))

		if is_uniq_article(article) and is_valid_article(article):
			# get people, look them up
			# add obj to current batch
			pass

	# send the data in the current batch to storage

	print("FIN")