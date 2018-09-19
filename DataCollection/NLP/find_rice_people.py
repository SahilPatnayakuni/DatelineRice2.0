# -*- coding: utf-8 -*-

#For init
#import nltk
#nltk.download('punkt')
import time
from newspaper import Article
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

PATH_TO_CLASSIFIER = '/Users/Alex/Desktop/COMP413/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
PATH_TO_JAR = '/Users/Alex/Desktop/COMP413/stanford-ner/stanford-ner.jar'

tagger = StanfordNERTagger(PATH_TO_CLASSIFIER, PATH_TO_JAR, encoding='utf-8')

def find_people(tagger, url):
	# Get article text using newspaper3k functions
	article = Article(url)
	article.download()
	article.parse()
	text = article.text

	# Tag all text using different categories
	tokenized_text = word_tokenize(text)
	classified_text = tagger.tag(tokenized_text)
	idx = 0
	all_people = []
	grouping = []

	# Find only the fields tagged with person
	while (idx < len(classified_text)):
		if (classified_text[idx][1] == 'PERSON'):
			grouping.append(classified_text[idx][0])
		else:
			if (grouping):
				all_people.append(grouping)
				grouping = []
		idx += 1

	if (grouping):
		all_people.append(grouping)

	return all_people


# Dan Wallach should be found in this article
# print(find_people(tagger, 'https://theconversation.com/4-ways-to-defend-democracy-and-protect-every-voters-ballot-101765'))

# Sam Solomon should be found in this article
# print(find_people(tagger, 'https://www.nbcnews.com/mach/science/climate-change-could-affect-human-evolution-here-s-how-ncna907276?cid=public-rss_20180907'))

# Jim Krane should be found in this article
# print(find_people(tagger, 'https://www.axios.com/saudi-arabia-touts-low-crude-oil-carbon-emissions-505c2c58-e776-48f8-9dd1-1020efed08fa.html'))
