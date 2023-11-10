import speech_recognition as sr
import oseti

def record_and_analyze_sentiment():
    # 音声認識の初期化
    recognizer = sr.Recognizer()
    sentiment_analyzer = oseti.Analyzer()

    with sr.Microphone() as source:
        print("10秒間の録音をおこなっています。")
        recognizer.adjust_for_ambient_noise(source)  # 環境ノイズの調整
        audio_data = recognizer.listen(source, timeout=10)  # 10秒間録音

        try:
            # 日本語での音声認識
            text = recognizer.recognize_google(audio_data, language='ja-JP')
            print(f"認識した文章: {text}")

            # 感情分析
            sentiment_scores = sentiment_analyzer.analyze(text)
            overall_sentiment = 1 if sum(sentiment_scores) > 0 else 0
            return overall_sentiment
        except Exception as e:
            print(f"Error: {e}")
            return None

# 実行
sentiment = record_and_analyze_sentiment()
print(f"Sentiment: {'Positive' if sentiment == 1 else 'Negative'}")
