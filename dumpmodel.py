import joblib
from classifier import MysteryClassifier
    

if __name__ == "__main__":
    # Create and fit the random classifier
    random_classifier = MysteryClassifier()
    random_classifier.fit(['Category A', 'Category B', 'Category C'])

    joblib.dump(random_classifier, 'model-serving-node/model.pkl')