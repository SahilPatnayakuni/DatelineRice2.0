# A super class that enforces all subclasses to
# implement the method classify.


class RiceMentionClassifier:
    def __init__(self):
        pass

    def predict(self, data_input):
        raise NotImplementedError

    def train(self):
        raise NotImplementedError

    def save_model(self):
        raise NotImplementedError

    def load_model(self):
        raise NotImplementedError
