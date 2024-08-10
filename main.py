from voice_command.py import listen_to_audio
from sentiment_analysis.py import analyze_sentiment
from response_generator.py import speak


def main():
    while True:
        spoken_text = listen_to_audio()

        if spoken_text:
            sentiment = analyze_sentiment(spoken_text)
            response = f"آپ کی گفتگو کا جذباتی رجحان: {sentiment}"
            speak(response)


if __name__ == "__main__":
    main()
