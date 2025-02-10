import mediapipe as mp
import cv2
import numpy as np
import uuid
import os

md_drawings = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0) # create a VideoCapture object

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=1) as hands: # create a hands object
    while cap.isOpened(): # while camera is active
        ret, frame = cap.read() # read the frame

        # Detect the hands
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # convert the frame to RGB
        image.flags.writeable = False # make the image read-only
        results = hands.process(image) # detect the hands
        image.flags.writeable = True # make the image writeable
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # convert the image back to BGR
        print(results)  

        # Draw the landmarks
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                md_drawings.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          md_drawings.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                                          md_drawings.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2),
                                          ) # landmarks

        cv2.imshow('Hand Tracking', frame) # display the frame

        if cv2.waitKey(10) & 0xFF == ord('q'): # if 'q' is pressed
            break # stop

cap.release() # delete the VideoCapture object
cv2.destroyAllWindows() # close all windows
