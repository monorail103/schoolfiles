import cv2
import numpy as np

# ベースメント
img1 = np.full((640, 480, 3), (0, 0, 0), np.uint8)

# 円
cv2.circle(img1, (240, 160), 100, (100, 0, 255), -1)

# 楕円
cv2.ellipse(img1, (200, 350), (300, 50), 0,0,360,(0,0,255), 3)

# 長方形
cv2.rectangle(img1, (100, 50), (200, 150), (255, 0, 0), 3)

# 正方形
cv2.rectangle(img1, (300, 50), (400, 150), (0, 255, 0), 3)

# 三角形
pts = np.array([[100, 200], [200, 200], [150, 100]])
cv2.polylines(img1, [pts], True, (255, 255, 0), 3)

cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()