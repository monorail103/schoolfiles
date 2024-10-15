import cv2
import pytesseract

# 画像を読み込む
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    # 必要に応じて画像を前処理（例: グレースケールに変換）
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 画像を表示
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # 文字認識を行う
        text = pytesseract.image_to_string(gray_image, lang='jpn')  # 日本語の場合

        # 認識したテキストをファイルに保存
        with open('recognized_text.txt', 'w', encoding='utf-8') as file:
            file.write(text)   
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break



# ウィンドウを閉じる
cv2.waitKey(0)
cv2.destroyAllWindows()