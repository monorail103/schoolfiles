import cv2
img = cv2.imread('img/Lenna.bmp', 1)

h, w, c = img.shape
print(h, w, c)

# 縮小
img_resize = cv2.resize(img, (200, 200), cv2.INTER_LINEAR)
cv2.imshow('img5', img_resize)
# 引き伸ばし
img_resize = cv2.resize(img, (w//2, h*2), cv2.INTER_LINEAR)
cv2.imshow('img1', img_resize)
img_resize = cv2.resize(img, (w*2, h//2), cv2.INTER_NEAREST)
cv2.imshow('img', img_resize)

# モザイク
scale = 0.2
dst = cv2.resize(img, (round(w*scale), round(h*scale)))
dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)
cv2.imshow('mosaic', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
