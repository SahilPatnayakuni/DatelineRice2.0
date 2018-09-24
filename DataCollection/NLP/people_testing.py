import scrape
import find_rice_people

PATH_TO_CLASSIFIER = '/Users/Alex/Desktop/COMP413/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
PATH_TO_JAR = '/Users/Alex/Desktop/COMP413/stanford-ner/stanford-ner.jar'
MAX_LINKS = 3 # controls the max number of links per article you look at
MAX_ARTICLES = 10 # controls the max number of articles per dateline you look at

ner_model = find_rice_people.NER_Model(PATH_TO_CLASSIFIER, PATH_TO_JAR)

main_urls = scrape.get_mainpage_links()
article_group = scrape.get_article_links(main_urls.pop())
num = 1

tagging_better = 0
tagging_same = 0
tagging_worse = 0

num_articles = min(MAX_ARTICLES, len(article_group))

for idx in range(0, num_articles):
	article = article_group[idx]
	print()
	print("Looking at at article #", num, " of ", num_articles)
	print("Number of links: ", len(article[1]))
	print("Looking through text....")
	descriptor_tags = find_rice_people.tag_people_with_text(article[0], ner_model)[1]
	link_tags = set([])
	link_num = 1

	print("Looking through links....")
	for link in article[1]:
		if (link_num == MAX_LINKS):
			break

		link_num += 1 
		link_tags = link_tags.union(find_rice_people.tag_people(link, ner_model)[1])

	# People tagging appearing from dateline but not from article tagging
	diff_set = descriptor_tags.difference(link_tags)

	if (len(diff_set) != 0):
		tagging_worse += 1
	elif (len(descriptor_tags) == len(link_tags)):
		tagging_same += 1
	else:
		tagging_better += 1

	num += 1


print("-------------------------------------------")
print("Out of ", len(article_group), " total articles:")
print(tagging_better, " articles were tagged better")
print(tagging_same, " articles were tagged the same")
print(tagging_worse, " articles were tagged worse")



