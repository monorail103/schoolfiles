import cv2

cap = cv2.VideoCapture(0)
eyecascade = cv2.CascadeClassifier("cascade/haarcascade_eye.xml")
facecascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_alt.xml")

while True:
    ret, frame = cap.read()
    face = facecascade.detectMultiScale(frame)

    if len(face) > 0:
        for x, y, w, h in face:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            eyes = eyecascade.detectMultiScale(frame[y:y+h, x:x+w])
            
            if len(eyes) > 0:
                for ex, ey, ew, eh in eyes:
                    cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 0, 255), 2)
    # else:
    #     print("No face detected")
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()