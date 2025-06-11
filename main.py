import cv2
from cvzone.HandTrackingModule import HandDetector
import time

time.sleep(2)

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9, maxHands=2)

while True:
    ret, frame = cap.read()
    if ret:
        hands, img = detector.findHands(frame)
        cv2.imshow("Hand Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()