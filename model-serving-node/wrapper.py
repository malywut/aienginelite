import joblib
#from classifier import MysteryClassifier

class MysteryClassifier(object):
    pass

class Wrapper(object):
    def __init__(self):
        pass
    
    def initialize(self):
        # Charger le modèle
        self.model = joblib.load('model.pkl')

    def predict(self, data):
        # Preparer les données pour la prediction
        data = data
        # Appeler la fonction de prediction
        return self.model.predict(data)
