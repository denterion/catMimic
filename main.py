import cv2 as cv
cap = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')



if not cap.isOpened():
    print("Нельзя открыть камеру")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Нельзя получить frame;(")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=4,
        minSize=(40, 40)
    )
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv.imshow('Webcam Feed', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()