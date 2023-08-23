import random

class MysteryClassifier(object):
    def __init__(self):
        self.classes = None

    def fit(self, classes):
        self.classes = classes

    def predict(self, X):
        predictions = random.choice(self.classes)
        return predictions