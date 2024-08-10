from model_loader import nlp_urdu

def analyze_sentiment(text):
    result = nlp_urdu(text)
    print(f"Sentiment Analysis Result: {result}")
    return result[0]['label']
