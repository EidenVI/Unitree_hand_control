import mediapipe as mp
import cv2
import numpy as np
import uuid
import os

md_drawings = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0) # only for macos

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=4) as hands:
    while cap.isOpened():
        ret, frame = cap.read()  # read the frame
        if not ret:
            print("Error: frame can not be read")
            break

        # Detect the hands
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert the frame to RGB
        image.flags.writeable = False  # make the image read-only
        results = hands.process(image)  # detect the hands
        image.flags.writeable = True  # make the image writeable
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # convert the image back to BGR
        print(results)

        # Draw the landmarks
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                md_drawings.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                            md_drawings.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=10),
                                            md_drawings.DrawingSpec(color=(255, 255, 255), thickness=4, circle_radius=4))
        cv2.imshow('Hand Tracking', image)  # display the processed image

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break  # stop

cap.release()  # delete the VideoCapture object
cv2.destroyAllWindows()  # close all windows