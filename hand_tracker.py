import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self, min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=1):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=min_detection_confidence,
                                         min_tracking_confidence=min_tracking_confidence,
                                         max_num_hands=max_num_hands)
        self.md_drawings = mp.solutions.drawing_utils

    def process_frame(self, frame):
        """
        Обрабатывает один кадр, выполняя обнаружение рук и создает их скелет

        :param frame: Входной кадр (изображение) в формате BGR.
        :return: Изображение с нарисованными ключевыми точками рук.
        """
        try:
            # Преобразование цвета
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = self.hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            #  Ключевые точки рук
            if results.multi_hand_landmarks:
                for hand in results.multi_hand_landmarks:
                    self.md_drawings.draw_landmarks(image, hand, self.mp_hands.HAND_CONNECTIONS,
                                                    self.md_drawings.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=10),
                                                    self.md_drawings.DrawingSpec(color=(255, 255, 255), thickness=4, circle_radius=4))
            return image, results  # Возвращаем как изображение, так и результаты
        except Exception as e:
            print(f"Error processing frame: {e}")
            return frame, None  # Возвращаем оригинальный кадр в случае ошибки