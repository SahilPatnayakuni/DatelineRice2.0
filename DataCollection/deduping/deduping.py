import re
from urllib.request import urlopen
import sys
sys.path.append("..")
from shared_types import ArticleData


def check_dup(article):
    url_set = query_urls()
    article_set = query_articles()
    if url_dup(article.url, url_set):  #case 1 + case 2 unshorten URL
        return True
    if check_meta_data(article, article_set):   #case 2
        return True




    #string edit distance call

    #tf/idf call


def query_urls():
    """
    Queries a list of urls that are currently already in the database
    :return: set of string urls
    """

    #currently hardcoded, will query later
    return set(["www.reddit.com"])

def query_articles():
    """
    Queries a list of articles that are already in the database for the last two weeks
    :return: list of ArticleData
    """

    #also hardcoded
    return [ArticleData("www.reddit.com",
                    "reddit",
                    "the front page of the internet",
                    "8/15/13",
                    "Bob",
                    "RedditEditor",
                    "oh wow, such a cool story I can't believe this is happening")]

def unshorten_url(url):
    """
    unshortern a url
    :param url: shortened url
    :return: unshortened url
    """

    request = urlopen(url)
    return request.geturl()

def url_dup(url, urlSet):
    """
    checks to see if a URL is duplicate

    :param url: url that is being checked
    :param urlSet: set of URL already in DB
    :return: true if url duplicate, else false
    """
    if url in urlSet:
        return True
    unshortened_url = unshorten_url(url)
    if unshortened_url in urlSet:
        return True
    return False

def check_attribute(attr1, attr2):
    """
    checks to see if attributes both are not None and also match
    :param attr1: first attribute being checked
    :param attr2: second attribute being checked
    :return:
    """
    return attr1 is not None and attr2 is not None and attr1 == attr2

def check_meta_two_art(article, article2):
    """
    Checks the metadata of two articles to see if they match
    :param article: first article being checked
    :param article2: second article check against
    :return:
    """
    if check_attribute(article.headline, article2.headline):
        return True
    if check_attribute(article.description, article2.description):
        return True
    if check_attribute(article.publication_date, article2.publication_date) and \
            check_attribute(article.authors, article2.authors):   # not sure if this should count? outlet??
        return True
    return False

def check_meta_data(article, article_set):
    """
    checks article against entire set of articles for meta data
    :param article: article being checked
    :param article_set: entire set of articles
    :return: True if article is duplicate, else false
    """
    for other_art in article_set:
        if check_meta_two_art(article, other_art):
            return True
    return False



def string_edit_check(content1, content2):
    """
    compute the string edit distance between two strings
    :param content1: first string being checked
    :param content2: secoind string being checked
    :return: string edit distance between two input strings
    """

    if not content1 and not content2:
        return -1 # some weird error
    if not content1:
        return len(content2)
    if not content2:
        return len(content1)

    dp_matrix = [[0 for j in range(len(content2))] for i in range(len(content1))]
    # print_matrix(dp_matrix)

    for i in range(len(content1)):
        dp_matrix[i][0] = i
    for j in range(len(content2)):
        dp_matrix[0][j] = j
    # print_matrix(dp_matrix)

    for i in range(1, len(content1)):
        for j in range(1, len(content2)):
            diagonal_match = dp_matrix[i - 1][j - 1] if content1[i] == content2[j] else dp_matrix[i - 1][j - 1] + 1
            dp_matrix[i][j] = min(dp_matrix[i - 1][j] + 1, dp_matrix[i][j-1] + 1, diagonal_match)
    # print_matrix(dp_matrix)
    if content1[i] != content2[j]:
        return dp_matrix[i][j] + 1
    else:
        return dp_matrix[i][j]

def print_matrix(matrix):
    print('---------------')
    for ele in matrix:
        print(ele)
    print('---------------')




def split(string):
    """
    Splits a string into words, to speed up string edit distance.
    """
    return list(filter(lambda x: x != ' ', re.split(r'(\b[^\s]+\b)', string)))

def isRice(string):
    """
    Returns T/F if a word is 'Rice'
    """
    return string == 'Rice' or string == 'rice' or string == 'Rice\'s'

def rice_idxs(data):
    """
    Returns a list of indices of 'rice' words in an article.
    """
    idxs = []
    for i in range(len(data)):
        if isRice(data[i]):
            idxs.append(i)
    return idxs

def score_idxs(string1, idx1, string2, idx2, rng = 100):
    """
    For two strings, and two indices into respective strings, returns the string
    edit distance between string1[idx1-rng:idx1+rng] and
    string2[idx2-rng:idx2+rng], normalized to portion of chars changed.
    """
    start1 = max(0, idx1 - rng)
    end1 = min(len(string1), idx1 + rng)
    start2 = max(0, idx2 - rng)
    end2 = min(len(string2), idx2 + rng)
    return string_edit_check(string1[start1:end1], string2[start2:end2])

def score_rices(string1, string2, rng = 100):
    """
    Returns the sum of scores over:
     - for each rice mention in string1:
      - find minimum string edit distance of that rice mention and any rice
        mention in string 2, +- rng characters
    Normalizes sum to portion of chars changed (0-1)
    """
    data1 = split(string1)
    data2 = split(string2)
    idxs1 = rice_idxs(data1)
    idxs2 = rice_idxs(data1)
    if len(idxs1) == 0 or len(idxs2) == 0:
        print('no rice mentions')
        return string_edit_check(data1, data2) / max(len(data1), len(data2))
    else:
        total = 0
        for idx1 in idxs1:
            min_match = float('inf')
            for idx2 in idxs2:
                min_match = min(min_match, score_idxs(data1, idx1, data2, idx2, rng))
            total += min_match
        return total * 1.0 / (len(idxs1) * rng * 2)


def score_split(string1, string2):
    """
    Scores string edit distance between words in string1 and words in string2.
    """
    data1 = re.split(r'(\b[^\s]+\b)', string1)
    data2 = re.split(r'(\b[^\s]+\b)', string2)
    data1 = list(filter(lambda x: x != ' ', data1))
    data2 = list(filter(lambda x: x != ' ', data2))
    return string_edit_check(data1, data2)

