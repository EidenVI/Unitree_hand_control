import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self, min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=1):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=min_detection_confidence,
                                         min_tracking_confidence=min_tracking_confidence,
                                         max_num_hands=max_num_hands)
        self.md_drawings = mp.solutions.drawing_utils
        
        """_summary_
        HandTracker class is responsible for detecting hands and creating its skeleton

            Attributes:
                self.mp_hands: mediapipe class for hands
                self.hands: mediapipe mp_hands's class object
                self.mp_drawings: mediapipe drawing utils object
                
            Parameters:
                min_detection_confidence: Minimum confidence value ([0.0, 1.0]) for hand detection to be considered successful
                min_tracking_confidence: Minimum confidence value ([0.0, 1.0]) for the hand landmarks to be considered tracked
                max_num_hands: Maximum number of hands to detect
            
        - We use the HandTracker class to process each frame and detect hands in the frame.
        """

    def process_frame(self, frame):
        """_summary_
        Process the frame -> detect hands -> draw landmarks
        
            Parameters:
                frame: frame to be processed
            
            Returns:
                image: frame with landmarks drawn
                results: landmarks coordinates
                
        - Used to create the skeleton of the hand in the frame
        """
        try:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = self.hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand in results.multi_hand_landmarks:
                    self.md_drawings.draw_landmarks(image, hand, self.mp_hands.HAND_CONNECTIONS,
                                                    self.md_drawings.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=10),
                                                    self.md_drawings.DrawingSpec(color=(255, 255, 255), thickness=4, circle_radius=4))
            return image, results
        except Exception as e:
            print(f"Error processing frame: {e}")
            return frame, None