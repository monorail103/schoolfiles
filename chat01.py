from transformers import pipeline
import csv

# 感情分析パイプラインを作成
sentiment_analysis = pipeline("sentiment-analysis", model="daigo/bert-base-japanese-sentiment")


# csvからテキストデータを読み込む
with open("chat_data.csv", newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # 各行を読み込む
    for row in reader:
        # テキストデータを取得
        text = row[0]
        
        # 感情分析を実行
        result = sentiment_analysis(text)[0]
        
        # 結果を表示
        print(f"Text: {text}")
        print(f"Label: {result['label']}, Score: {result['score']}")
