# 各拡張子で保存
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img/Aerial.bmp', 1)
cv2.imshow('image', img)
# JPGで保存
cv2.imwrite('img/Aerial.jpg', img)
# PNGで保存
cv2.imwrite('img/Aerial.png', img)
# tiffで保存
cv2.imwrite('img/Aerial.tiff', img)
cv2.waitKey(0)
cv2.destroyAllWindows()