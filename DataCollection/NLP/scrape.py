from bs4 import BeautifulSoup
import requests, sys
from newspaper import Article

def get_mainpage_links():
	print("Getting main page links...")
	page_link = 'http://news.rice.edu/category/datelinrice/'
	page_response = requests.get(page_link, timeout=5)
	page_content = BeautifulSoup(page_response.content, "html.parser")

	urls = set()

	for a_tag in page_content.find_all("a"):
		link = str(a_tag.get('href'))
		if link and '/2018/' in link and 'dateline-rice-for' in link:
			urls.add(link)

	return urls

def get_article_links(article):
	print("Getting article links for " + article)
	page_link = article
	page_response = requests.get(page_link, timeout=5)
	page_content = BeautifulSoup(page_response.content, "html.parser")

	list_articles = []

	for body_text in page_content.find_all("p"):
		urls = set()

		for br in body_text.find_all("br"):
			br.replace_with("")

		for a_tag in body_text.find_all("a"):
			link = str(a_tag.get('href'))
			if link and 'http' in link and 'news.rice' not in link:
				urls.add(link)

		if(len(urls) == 0):
			continue;

		while(body_text.strong):
			body_text.strong.decompose()
			
		while(body_text.em):
			body_text.em.decompose()

		while(body_text.a):
			body_text.a.decompose()

		string_text = str(body_text).replace("\n", "").replace("<p>", "").replace("</p>", "")
		list_articles.append((string_text, urls))

	return list_articles