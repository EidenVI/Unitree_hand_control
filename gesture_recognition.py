import mediapipe as mp

mp_hands = mp.solutions.hands
hands  = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)


def recognize_gesture(hand_landmarks):
    # Recognize gestures
    if hand_landmarks is not None:
        # Get the landmarks
        landmarks = hand_landmarks.landmark
        # Get the thumb landmarks
        thumb = landmarks[4]
        index = landmarks[8]
        middle = landmarks[12]
        ring = landmarks[16]
        pinky = landmarks[20]

        # Check the thumb and index finger
        if thumb.y < index.y:
            if thumb.x < index.x:
                return "L"
            else:
                return "R"
        # Check the index and middle finger
        if index.y < middle.y:
            if index.x < middle.x:
                return "U"
            else:
                return "D"
        # Check the middle and ring finger
        if middle.y < ring.y:
            if middle.x < ring.x:
                return "S"
            else:
                return "P"
        # Check the ring and pinky finger
        if ring.y < pinky.y:
            if ring.x < pinky.x:
                return "O"
            else:
                return "C"