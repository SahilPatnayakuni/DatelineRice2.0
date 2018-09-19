# A super class that enforces all subclasses to
# implement the method classify.
from abc import ABC, abstractmethod

class RiceMentionClassifier(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def classify(self, data_input):
        pass