import cv2
from cvzone.HandTrackingModule import HandDetector  # cvzone version: 1.5.0

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand1 = hands[0]
        landmark_list1 = hand1["lmList"]
        bounding_box1 = hand1["bbox"]
        centre_point1 = hand1["center"]
        hand_type1 = hand1["type"]

        fingers1 = detector.fingersUp(hand1)
        # length, info, img = detector.findDistance(landmark_list1[8], landmark_list1[12], img)
        # length, info = detector.findDistance(landmark_list1[8], landmark_list1[12])

        if len(hands) == 2:
            hand2 = hands[1]
            landmark_list2 = hand2["lmList"]
            bounding_box2 = hand2["bbox"]
            centre_point2 = hand2["center"]
            hand_type2 = hand2["type"]

            fingers2 = detector.fingersUp(hand2)

            print(fingers1, fingers2)
            # length, info, img = detector.findDistance(landmark_list1[8], landmark_list2[8], img)
            length, info, img = detector.findDistance(centre_point1, centre_point2, img)


    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
