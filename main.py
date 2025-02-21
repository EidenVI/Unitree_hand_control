import cv2
from hand_tracker import HandTracker
from utils import initialize_camera
from gesture_recognition import recognize_gesture

def main():
    try:
        cap = initialize_camera()
    except Exception as e:
        print(f"Error initializing camera: {e}")
        return

    hand_tracker = HandTracker()
    
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Error: frame cannot be read")
                break
            
            frame = cv2.flip(frame, 1)
            processed_frame, results = hand_tracker.process_frame(frame)
            
            if results and results.multi_hand_landmarks:
                for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                    hand_type = handedness.classification[0].label
                    gesture = recognize_gesture(hand_landmarks, hand_type)
                    if gesture:
                        cv2.putText(processed_frame, gesture, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.imshow('Hand Tracking', processed_frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"Error during processing: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()