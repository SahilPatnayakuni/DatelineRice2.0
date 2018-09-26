"""
Rice Mention Classifier Tester
- In order to run use cmd
    python3 -m RiceMention.test.runner {name of the classifier desired to be tested}
- Run classifier(s) on test data set and calculate accuracy for each one.
"""
import argparse
import sys

from RiceMention.classifiers.binary_classifiers import *
from .test_data import dummy_data, dummy_label


def get_classifier(name):
    """
    Input:
    - name : A string of the name of the classifier wanted to be tested.
    - args : TODO add args parameter for some classifiers that require args.

    Given the name of the classifier the user wants to test,
    return the instance of that classifier.
    """
    return getattr(sys.modules[__name__], name)()

# User input definition
parser = argparse.ArgumentParser(description='Rice Mention Classifier Tester')
parser.add_argument('name', type=str, help='The class name of the classifier')
# TODO add more flags
# parser.add_argument('--ensemble', default=False) # To use ensemble or not
# parser.add_argument('--threshold', type=int, default=0.5) # threshold for the ensemble
# parser.add_argument() # take in arguments for specific classifiers

if __name__ == '__main__':
    args = parser.parse_args()
    # search for classifier given in the user argument
    classifier = get_classifier(args.name)
    num_correct = 0 # num of accurate classifications
    num_fp = 0 # num of false positives
    for i in range(len(dummy_label)):
        result = classifier.classify(dummy_data[i])
        if dummy_label[i] == result:
            num_correct += result
        else:
            if dummy_label[i] == 0:
                # false positive detected
                num_fp += 1

    accuracy = num_correct / len(dummy_label)
    print("Accuracy : {accuracy}".format(**locals()))
    print("False positives : {num_fp}".format(**locals()))