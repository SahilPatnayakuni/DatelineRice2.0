"""
Data scrapper. 
- Scrapes invalid, valid article texts.
- Store scraped results in npz format.
"""
import argparse
from bs4 import BeautifulSoup
import requests, sys
from newspaper import Article
from invalid_urls import invalid_text_urls
import numpy as np


DATELINE_LINK = 'http://news.rice.edu/category/datelinrice/page/'

class ValidDataScraper:
    def __init__(self, page_num_max=100):
        self.page_num_max = page_num_max

    def get_mainpage_links(self):
        print("Getting main page links...")

        page_num = 1
        urls = set()

        while page_num < self.page_num_max:
            page_link = DATELINE_LINK + str(page_num)
            page_response = requests.get(page_link, timeout=5)
            if (page_response.status_code == 404):
                break
            page_content = BeautifulSoup(page_response.content, "html.parser")

            for a_tag in page_content.find_all("a"):
                link = str(a_tag.get('href'))
                if link and 'dateline-rice-for' in link:
                    urls.add(link)
            page_num += 1
        return urls        

    def get_article_links(self, article):
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

    
    def get_prev_dateline(self, num=2742):
        main_urls = self.get_mainpage_links()
        x_train = []
        i = 0

        try:
            for url in main_urls:
                curr_article_links = self.get_article_links(url)

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


class InvalidDataScraper:

    def __init__(self):
        pass
    
    def get_invalid(self):
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


parser = argparse.ArgumentParser(description='Dateline Scraper')
parser.add_argument('--valid',
    action='store_true',
    help='Scrape valid articles flag' )
parser.add_argument('--invalid',
    action='store_true',
    help='Scrape invalid articles flag' )
# TODO concatenate flag - default overwrite.
# TODO date range


if __name__ == "__main__":
    args = parser.parse_args()
    if args.valid:
        scraper = ValidDataScraper(page_num_max=100)
        scraper.get_prev_dateline()
    if args.invalid:
        scraper = InvalidDataScraper()
        scraper.get_invalid()




