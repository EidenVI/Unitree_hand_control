import cv2
from hand_tracker import HandTracker
from utils import initialize_camera
from gesture_recognition import recognize_gesture

def main():
    cap = initialize_camera()
    hand_tracker = HandTracker()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: frame cannot be read")
            break
        
        processed_frame, results = hand_tracker.process_frame(frame)

        if results and results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                gesture = recognize_gesture(hand_landmarks)
                if gesture:
                    print(f"Gesture recognized: {gesture}")

        cv2.imshow('Hand Tracking', processed_frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()