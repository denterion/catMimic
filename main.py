import cv2 as cv
cap = cv.VideoCapture(0)



if not cap.isOpened():
    print("Нельзя открыть камеру")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Нельзя получить frame;(")
        break
    
    cv.imshow('Webcam Feed', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()