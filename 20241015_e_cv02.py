# 画像にタイトルを入れる
import cv2

img = cv2.imread('img/Aerial.bmp', 1)
# タイトルいれる
cv2.putText(img, 'Aerial.bmp', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('image', img)
# JPGで保存
cv2.imwrite('img/Aerial_title.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()