import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_alt.xml")
    face = cascade.detectMultiScale(frame)

    if len(face) > 0:
        for x, y, w, h in face:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    # else:
    #     print("No face detected")
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()