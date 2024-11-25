import cv2
import pyautogui

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_alt.xml')

# スクリーンの中心座標を取得
screen_width, screen_height = pyautogui.size()
screen_center_x = screen_width // 2
screen_center_y = screen_height // 2

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 顔検出
    faces = cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        # 最も大きい顔を選択
        largest_face = max(faces, key=lambda face: face[2] * face[3])
        x, y, w, h = largest_face

        # 顔の中心座標を計算
        face_center_x = x + w // 2
        face_center_y = y + h // 2

        # 画面の中心座標と顔の中心座標の差を取得
        diff_x = face_center_x - screen_center_x
        diff_y = face_center_y - screen_center_y

        # 差を移動量に変換（スケールを調整）
        move_x = diff_x // 10
        move_y = diff_y // 10

        # マウスを移動
        pyautogui.moveRel(move_x, move_y)

        # 顔を囲む（デバッグ用）
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()