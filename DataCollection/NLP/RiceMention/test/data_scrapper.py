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
from datetime import datetime, timedelta
import numpy as np


DATELINE_LINK = 'http://news.rice.edu/category/datelinrice/page/'
DATELINE_HEADER = 'http://news.rice.edu/'
DATE_FORMAT = '%Y/%m/%d'

class ValidDataScraper:
    def __init__(self, start_date, end_date, file_name, page_num_max=100):
        self.page_num_max = page_num_max
        self.start_date = start_date
        self.end_date = end_date
        self.file_name = file_name

    def get_mainpage_links(self):
        """
        Input: 
            - start_date : A str style of 2018/07/01
            - end_date : same as start_date
        Output:
            - http://news.rice.edu/{YYYY}/{MM}/{DD}/dateline-rice-for*
        """
        urls = set()

        start = datetime.strptime(self.start_date, DATE_FORMAT)
        end = datetime.strptime(self.end_date, DATE_FORMAT)

        while start < end:
            urls.add(DATELINE_HEADER + start.strftime(DATE_FORMAT) + '/dateline-rice-for*')
            start = start + timedelta(days=1)

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

        np.savez('{file_name}.npz'.format(file_name=self.file_name), text=x_train) # use the date range and concatenate flag
        print("Valid dataset ready.")
        

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
            except KeyboardInterrupt:
                print("Caught keyboard interrupt, exiting")
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
        np.savez('invalid_texts.npz', text=x_train)
        print("Invalid dataset ready.")


parser = argparse.ArgumentParser(description='Dateline Scraper')
parser.add_argument('--valid',
    action='store_true',
    help='Scrape valid articles flag' )
parser.add_argument('--invalid',
    action='store_true',
    help='Scrape invalid articles flag' )
parser.add_argument('start_date', type=str, help='The start date in the format of {YYYY}/{MM}/{DD}')
parser.add_argument('end_date', type=str, help='The end date in the format of {YYYY}/{MM}/{DD}')
parser.add_argument('valid_file', type=str, help='The name of the valid dataset file')

if __name__ == "__main__":
    args = parser.parse_args()
    if args.valid:
        scraper = ValidDataScraper(
            start_date=args.start_date, 
            end_date=args.end_date,
            file_name=args.valid_file
        )
        scraper.get_prev_dateline()
    if args.invalid:
        scraper = InvalidDataScraper()
        scraper.get_invalid()




