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

	urls = set()

	for a_tag in page_content.find_all("a"):
		link = str(a_tag. get('href'))
		if link and 'http://bit.ly' in link:
			urls.add(link)

	return urls

if __name__ == "__main__":
	main_urls = get_mainpage_links()

	for url in main_urls:
		curr_article_links = get_article_links(url)

		for link in curr_article_links:
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