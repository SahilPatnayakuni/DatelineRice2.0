from urllib.request import urlopen

class Article:   # copied over from search_rss_shared.py
    def __init__(self, url=None, title=None, description=None, publicationDate=None, authors=None):
        self.url = url
        self.title = title
        self.description = description
        self.publicationDate = publicationDate
        self.authors = authors



def check_dup(article):
    url_set = query_urls()
    article_set = query_articles()
    if url_dup(article.url, url_set):  #case 1
        return True
    if  check_meta_data(article, article_set):   #case 2
        return True
    if url_dup(unshorten_url(article.url), url_set):  #case 2, unshortern URL
        return True

    #string edit distance call

    #tf/idf call


def query_urls():
    #currently hardcoded, will query later
    return set(["www.reddit.com"])

def query_articles():
    #also hardcoded
    return [Article("www.reddit.com",
                    "reddit",
                    "the front page of the internet",
                    "8/15/13",
                    "Bob")]

def url_dup(url, urlSet):
    if url in urlSet:
        return True

def check_attribute(attr1, attr2):
    return attr1 is not None and attr2 is not None and attr1 == attr2

def check_meta_two_art(article, article2):
    if check_attribute(article.title, article2.title):
        return True
    if check_attribute(article.description, article2.description):
        return True
    if check_attribute(article.publicationDate, article2.publicationDate) and \
            check_attribute(article.authors, article2.authors):   # not sure if this should count?
        return True
    return False

def check_meta_data(article, article_set):
    for other_art in  article_set:
        if check_meta_two_art(article, other_art):
            return True
    return False

def unshorten_url(url):
    request = urlopen(url)
    return request.geturl()



def string_edit_check(content1, content2):

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




def testing():
    print("#1:", string_edit_check("abcfeg", "xabcdeg") == 2)
    print("#2:", string_edit_check("", "xcdeg") == 5)
    print("#3:", string_edit_check("123123456", "123456") == 3)

    print("4:", unshorten_url("http://www.youtube.com"))
    # print('w')
    print("5:", unshorten_url("http://y2u.be/j4dMnAPZu70") == "https://www.youtube.com/watch?v=j4dMnAPZu70")
    print("6:", unshorten_url("https://bit.ly/2NhJtop"))
    print("7:", unshorten_url("https://www.youtube.com/watch?v=j4dMnAPZu70"))


testing()

