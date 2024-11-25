import cv2
import numpy as np
import pyautogui
import mediapipe as mp

# landmarkの繋がり表示用
landmark_line_ids = [ 
    (0, 1), (1, 5), (5, 9), (9, 13), (13, 17), (17, 0),  # 掌
    (1, 2), (2, 3), (3, 4),         # 親指
    (5, 6), (6, 7), (7, 8),         # 人差し指
    (9, 10), (10, 11), (11, 12),    # 中指
    (13, 14), (14, 15), (15, 16),   # 薬指
    (17, 18), (18, 19), (19, 20),   # 小指
]

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,                # 最大検出数
    min_detection_confidence=0.7,   # 検出信頼度
    min_tracking_confidence=0.7     # 追跡信頼度
)

cap = cv2.VideoCapture(0)   # カメラのID指定

# マウスのスクリーンサイズ取得
screen_w, screen_h = pyautogui.size()

# 親指の前フレームの位置を保存する変数
prev_thumb_x, prev_thumb_y = None, None

# クリック判定のしきい値（ピクセル単位）
click_threshold = 20

while True:
    # カメラから画像取得
    success, img = cap.read()
    if not success:
        continue
    img = cv2.flip(img, 1)          # 画像を左右反転

    # 画像のサイズを取得
    img_h, img_w, _ = img.shape

    # 検出処理の実行
    results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks:
        # 検出した手の数分繰り返し
        for hand_landmarks in results.multi_hand_landmarks:
            for i, lm in enumerate(hand_landmarks.landmark):
                if i == 8:
                    # 人差し指の位置の座標
                    lmx = int(lm.x * img_w)
                    lmy = int(lm.y * img_h)
                    # 人差し指の位置に円
                    cv2.circle(img, (lmx, lmy), 3, (255, 0, 0), -1)

                    # 人差し指の位置をスクリーンサイズにマッピング
                    mouse_x = int(lm.x * screen_w)
                    mouse_y = int(lm.y * screen_h)  # y座標は上下反転するため

                    # マウスを動かす
                    pyautogui.moveTo(mouse_x, mouse_y)

                elif i == 4:
                    # 親指の位置の座標
                    thumb_x = int(lm.x * img_w)
                    thumb_y = int(lm.y * img_h)
                    # 親指の位置に円
                    cv2.circle(img, (thumb_x, thumb_y), 3, (0, 255, 0), -1)

                    # 親指の位置をスクリーンサイズにマッピング
                    mouse_thumb_x = int(lm.x * screen_w)
                    mouse_thumb_y = int(lm.y * screen_h)

                    # 前フレームの親指の位置がある場合、クリック判定を行う
                    if prev_thumb_x is not None and prev_thumb_y is not None:
                        # 親指の動きを計算
                        thumb_movement = np.sqrt((thumb_x - prev_thumb_x) ** 2 + (thumb_y - prev_thumb_y) ** 2)

                        # クリックしきい値を超えた場合、クリックを発生させる
                        if thumb_movement > click_threshold:
                            pyautogui.click()
                            print("Clicked!")

                    # 現在の親指の位置を保存
                    prev_thumb_x, prev_thumb_y = thumb_x, thumb_y

    # 画像の表示
    cv2.imshow("MediaPipe Hands", img)
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()