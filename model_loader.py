from transformers import pipeline

def load_model():
    # Load the sentiment analysis model once and return it
    return pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Initialize the model
nlp_urdu = load_model()
