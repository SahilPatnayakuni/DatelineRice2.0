from bs4 import BeautifulSoup
import requests, sys
from newspaper import Article
from invalid_urls import invalid_text_urls
import numpy as np

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

def get_prev_dateline(num=2742):
    main_urls = get_mainpage_links()
    x_train = []
    i = 0

    try:
        for url in main_urls:
            curr_article_links = get_article_links(url)

            for link in curr_article_links:
                if num is not None and i == num:
                    print(f"acquired {i} number of documents exiting")
                    raise KeyboardInterrupt
                try:      
                    article = Article(link)
                    article.download()
                    article.parse()
                except KeyboardInterrupt:
                    raise KeyboardInterrupt
                except Exception as e:
                    print('{} occured'.format(e))
                    continue
                print(f"{i}. {link}")   
                text = article.text
                if text != '':
                    i += 1
                    x_train.append(article.text)
                else:
                    print('no valid text found')
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")

    np.savez(f'valid_texts{i}.npz', text=x_train)

def get_invalid():
    x_train = []
    i = 0
    for link in invalid_text_urls:
        try:      
            article = Article(link)
            article.download()
            article.parse()
        except:
            continue
        print(f"{i}. {link}")  
        text = article.text
        if text != '':
            i += 1
            x_train.append(article.text)
        else:
            print('no valid text found')
    np.savez('invalid_texts.npz', text=x_train)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--prev":
            get_prev_dateline()
        elif sys.argv[1] == "--invalid":
            get_invalid()  
