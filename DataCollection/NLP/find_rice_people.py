# -*- coding: utf-8 -*-

#For init
#import nltk
#nltk.download('punkt')
import time
from newspaper import Article
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import people_api_extractor as pae

PATH_TO_CLASSIFIER = '/Users/Alex/Desktop/COMP413/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
PATH_TO_JAR = '/Users/Alex/Desktop/COMP413/stanford-ner/stanford-ner.jar'

class NER_Model:
	def __init__(self, path_to_classifier, path_to_jar):
		self.tagger = StanfordNERTagger(path_to_classifier, path_to_jar, encoding='utf-8') 

def find_people(url, ner_model):
	# Get article text using newspaper3k functions
	try:
		article = Article(url)
		article.download()
		article.parse()
		text = article.text
	except Exception as e:
		print("Something went wrong parsing link")
		return set([])

	return find_people_using_text(text, ner_model)

def find_people_using_text(text, ner_model):
	# Tag all text using different categories
	tokenized_text = word_tokenize(text)
	classified_text = ner_model.tagger.tag(tokenized_text)

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

def tag_people(article, ner_model):
	people_list = find_people(article, ner_model)
	correct_match = []
	net_id_set = set([])

	for people in people_list:
		if (len(people) >= 2):
			match = pae.matches(people[0], people[-1])
			if (match['result']['people']):
				print("Found person: ", people)
				correct_match.append(match['result']['people'][0])
				net_id_set.add(match['result']['people'][0]['netid'])
			else:
				print("Could not find: ", people)

	return (correct_match,net_id_set)

def tag_people_with_text(text, ner_model):
	people_list = find_people_using_text(text, ner_model)
	correct_match = []
	net_id_set = set([])

	for people in people_list:
		if (len(people) >= 2):
			match = pae.matches(people[0], people[-1])
			if (match['result']['people']):
				print("Found person: ", people)
				correct_match.append(match['result']['people'][0])
				net_id_set.add(match['result']['people'][0]['netid'])
			else:
				print("Could not find: ", people)

	return (correct_match, net_id_set)
