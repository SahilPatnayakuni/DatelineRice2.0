from .RiceMentionClassifier import RiceMentionClassifier
from collections import defaultdict
import string

class ContainsRiceClassifier(RiceMentionClassifier):
    def __init__(self):
        pass

    def classify(self, data_input):
        return "Rice" in data_input['body-text']

class ContainsRiceUniversityClassifier(RiceMentionClassifier):
    def __init__(self):
        pass

    def classify(self, data_input):
        return "Rice University" in data_input['body-text']


class UnweightedEnsembleModel(RiceMentionClassifier):
    def __init__(self, classifiers, threshold):
        self.classifiers = classifiers
        self.threshold = threshold
    
    def classify(self, data_input):
        count = 0
        for classifier in self.classifiers:
            count += classifier.classify(data_input)
        return count / len(self.classifiers) >= self.threshold

class NaiveClassifier(RiceMentionClassifier):
    def __init__(self):
        self.rice_words = set(['grain', 'fried', 'bowl', 'white', 'boiled', 'boil', 'steamed', 'steam' 'cook', 'eat', 'ate', 'paddy', 'pudding', 'delicious'])

        self.academic_words = set(['professor', 'dr', 'school', 'college', 'department', 'engineering', 'science', 'mathematics', 'statistics', 'history', 'studies', 'english', 'philosophy', 'jewish', 'medieval', 'politics', 'political', 'religion', 'chemistry', 'kinesiology', 'physics', 'astronomy', 'anthropology', 'economics', 'linguistics', 'psychology', 'sociology'])

        self.threshold = .2  # Pretty sure the statistic is in [-1, 1]


    @staticmethod
    def tokenize(input_str):
        """ 
        Remove punctuation and split on whitespace.
        Returns list of strings. 
        """
        words = input_str.split()  # Split on all whitespace
        # Remove punctuation
        table = input_str.maketrans('', '', string.punctuation)
        stripped = [word.translate(table) for word in words]
        return stripped
    
    @staticmethod
    def get_count_dict(str_list):
        """ Returns a dictionary mapping words to their counts in str. """
        count_dict = defaultdict(int)
        for item in str_list:
            count_dict[item] += 1
        return count_dict

    def classify(self, data_input):
        body = data_input['body-text']
        words = NaiveClassifier.tokenize(body)
        count_dict = NaiveClassifier.get_count_dict(words)

        length = len(words)
        
        # Now we compute some arbitrary statistics, normalized.
        Rice_counts = count_dict['Rice'] / length
        rice_counts = count_dict['rice'] / length
        Rice_University_counts = 0
        for i in range(len(words) - 1):
            if words[i] == 'Rice' and words[i+1] == 'University':
                Rice_University_counts += 1
        Rice_University_counts /= length
        Village_counts = count_dict['Village'] / length
        
        body_lower = body.lower()
        words_lower = NaiveClassifier.tokenize(body_lower)

        rice_related_counts = 0
        for word in words_lower:
            if word in self.rice_words:
                rice_related_counts += 1
        rice_related_counts /= length

        academic_counts = 0
        for word in words_lower:
            if word in self.academic_words:
                academic_counts += 1
        academic_counts /= length

        # Take the linear combination of these
        score = Rice_counts + Rice_University_counts + academic_counts - rice_counts - Village_counts - rice_related_counts
        score /= 6  # Normalize by num of stats
        return score > self.threshold
        
        