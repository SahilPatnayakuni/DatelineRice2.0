from bs4 import BeautifulSoup
from newspaper import Article
import requests, sys, webhoseio
import sys

sys.path.append("..")
from shared_types import *
sys.path.pop()

return_objs = []

current_batch_objs = list()
search_terms = ['rice university']

for term in search_terms:
	# make response diff based on search terms

	response = requests.get("https://api.newsriver.io/v2/search?query=text%3A%22rice%20university%22%20OR%20title%3A%22rice%20university%22&sortBy=discoverDate&sortOrder=DESC&limit=15", headers={"Authorization":"sBBqsGXiYgF0Db5OV5tAw-SV99gJE88m8wacCchf2-RRrEiOATHNTquKXyn2goTIn2pHZrSf1gT2PUujH1YaQA"})
	jsonFile = response.json()
	for resp in jsonFile:
		url = resp['url']
		title = None
		highlight = None
		publishDate = None
		siteName = None
		domainName = None
		text = None

		source = requests.get(url, timeout=5)
		BS = BeautifulSoup(source.content, "html.parser")
		article = Article(source.url)
		article.download()
		article.parse()

		try:
			title = resp['title']
		except Exception as e:
			pass

		try:
			highlight = resp['highlight']
		except Exception as e:
			pass

		try:
			publishDate = resp['publishDate']
		except Exception as e:
			pass

		try:
			siteName = resp['website']['name']
		except Exception as e:
			pass

		try:
			domainName = resp['website']['domainName']
		except Exception as e:
			pass

		try:
			text = resp['text']
		except Exception as e:
			pass

		article_obj = ArticleData(url, title, highlight, publishDate, article.authors, Outlet(siteName, None, None, None, domainName), text)
		print("newsriver" + str(article_obj.to_json()))
		return_objs.append(article_obj)

	webhoseio.config(token="25ad10f0-486b-408b-a8d2-0709e56808ce")
	query_params = {
	    "q": "\"rice university\"", # make this different based on search terms
	    "ts": "1536006194344",
	    "sort": "published"
	}

	output = webhoseio.query("filterWebContent", query_params)
	total_results = output['totalResults']
	counter = int(1 + total_results / 100)

	for i in range(counter):
	    for j in range(100):
	        try:
	            url = output['posts'][j]['thread']['url']
	            authors = None
	            title = None
	            highlight = None
	            publishDate = None
	            siteName = None
	            domainName = None
	            text = None

	            try:
	            	authors = output['posts'][j]['author']
	            except Exception as e:
	            	pass

	            try:
	            	title = output['posts'][j]['title']
	            except Exception as e:
	            	pass

	            try:
	            	highlight = output['posts'][j]['url']
	            except Exception as e:
	            	pass

	            try:
	            	publishDate = output['posts'][j]['published']
	            except Exception as e:
	            	pass

	            try:
	            	domainName = output['posts'][j]['thread']['site']
	            except Exception as e:
	            	pass

	            try:
	            	text = output['posts'][j]['text']
	            except Exception as e:
	            	pass

	            if authors == None:
	            	source = requests.get(url, timeout=5)
	            	BS = BeautifulSoup(source.content, "html.parser")
	            	article = Article(source.url)
	            	article.download()
	            	article.parse()
	            	authors = article.authors

	            article_obj = ArticleData(url, title, highlight, publishDate, authors, Outlet(None, None, None, None, domainName), text)
	            print("webhose" + str(article_obj.to_json()))
	            return_objs.append(article_obj)

	        except Exception as e:
	        	break

	        output = webhoseio.get_next()

print(return_objs)

# article = Article(source.url)
# article.download()
# article.parse()
# article.nlp()

# print(article.text)
# print("LINK: " + link + "\n")
# print("URL: " + source.url + "\n")
# print("AUTHORS: " + str(article.authors) + "\n")
# print("PUBLISH DATE: " + str(article.publish_date) + "\n")
# print("KEYWORDS: " + str(article.keywords) + "\n")
# print("SUMMARY: " + str(article.summary) + "\n")