# A super class that enforces all subclasses to
# implement the method classify.
from abc import ABC, abstractmethod

class RiceMentionClassifier(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def save_model(self):
        pass
    
    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def predict(self, input):
        pass

    def load_data(self):
        # TODO
        pass

    def get_train(self):
        return self.train_data

    def get_test(self):
        return self.test_data

    def get_validation(self):
        return self.validation 

    def __call__(self, input):
        return self.predict(input)
    
    def k_fold(self, num_folds):
        # TODO
        pass