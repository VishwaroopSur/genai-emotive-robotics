from textblob import TextBlob

def detect_emotion(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity < -0.2:
        return "Sad"
    elif polarity > 0.2:
        return "Happy"
    else:
        return "Neutral"
