# 各拡張子で保存
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img/Lenna.bmp', 1)

red = img.copy()
red[:, :, 0] = 0
red[:, :, 1] = 0

green = img.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0

blue = img.copy()
blue[:, :, 1] = 0
blue[:, :, 2] = 0

cv2.imshow('red', red)
cv2.imshow('green', green)
cv2.imshow('blue', blue)

cv2.imwrite('img/Lenna_red.jpg', red)
cv2.imwrite('img/Lenna_green.jpg', green)
cv2.imwrite('img/Lenna_blue.jpg', blue)
cv2.waitKey(0)
cv2.destroyAllWindows()