from RiceMention.core.classifer import RiceMentionClassifier


class Pipeline(RiceMentionClassifier):
    def __init__(self):
        """
        init everything
        """
        super(Pipeline, self).__init__()

    def _load_data(self, filepath=None, scape=False):
        """
        if filepath:
            # Load data

        Scrape data if needed
        :param filepath:
        :return:
        """

    def get_splits(self):
        """
        Generator that spits out train/validation splits
        Use KFold
        :return:
        """

    def evaluate(self):
        """
        Runs classifier on test dataset
        :return:
        """

    def run(self, json_input):
        """
        super(Pipeline, self).predict(processdata)
        :param json_input:
        :return:
        """

    def process_data(self):
        """
        PRocess data
        :return:
        """