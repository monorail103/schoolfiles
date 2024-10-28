import cv2

img = cv2.imread('img/Couple.bmp', 1)

# トリミング
img_trim = img[0:300, 0:150]
cv2.imshow('image', img_trim)
cv2.imwrite('img/Couple_trim.jpg', img_trim)
cv2.waitKey(0)
cv2.destroyAllWindows()