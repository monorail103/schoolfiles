import cv2

img = cv2.imread("image02/flower02.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def nothing(x):
    pass

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.createTrackBar("H-Low", 'img', 0, 179, nothing)
cv2.createTrackBar("S-Low", 'img', 0, 255, nothing)
cv2.createTrackBar("V-Low", 'img', 0, 255, nothing)
cv2.createTrackBar("H-Up", 'img', 179, 179, nothing)
cv2.createTrackBar("S-Up", 'img', 255, 255, nothing)
cv2.createTrackBar("V-Up", 'img', 255, 255, nothing)

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break

    HL = cv2.getTrackbarPos("H-Low", "HSV")
    SL = cv2.getTrackbarPos("S-Low", "HSV")
    VL = cv2.getTrackbarPos("V-Low", "HSV")
    lower = (HL, SL, VL)
    HU = cv2.getTrackbarPos("H-Up", "HSV")
    SU = cv2.getTrackbarPos("S-Up", "HSV")
    VU = cv2.getTrackbarPos("V-Up", "HSV")
    upper = (HU, SU, VU)
    bin_img = cv2.inRange(hsv, lower, upper)
    cv2.imshow("img", bin_img)

cv2.destroyAllWindows()