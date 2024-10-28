import cv2
import numpy as np

# ベースメント
img1 = np.full((640, 480, 3), (255, 255, 255), np.uint8)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (128, 0, 128), (128, 128, 0), (0, 128, 128)]
for i in range(9):
    top_left = (i * 50 + 10, i * 50 + 10)
    bottom_right = (i * 50 + 60, i * 50 + 100)
    color = colors[i % len(colors)]
    cv2.rectangle(img1, top_left, bottom_right, color, -1)

cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()