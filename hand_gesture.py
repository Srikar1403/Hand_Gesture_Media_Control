# import cv2
# import mediapipe as mp
# import pyautogui
# import time

# # Function to calculate fingertip distance
# def calculate_distance(p1, p2):
#     return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

# # Function to count fingers and track tip positions
# def track_fingers(hand_landmarks):
#     finger_tips = []
#     finger_count = 0

#     threshold = (hand_landmarks.landmark[0].y * 100 - hand_landmarks.landmark[9].y * 100) / 2

#     for idx, landmark in enumerate(hand_landmarks.landmark):
#         if (idx == 4 or idx == 8):  # Check for index and middle finger tips
#             finger_tips.append(landmark)
#             if (hand_landmarks.landmark[idx + 5].y * 100 - hand_landmarks.landmark[idx].y * 100) > threshold:
#                 finger_count += 1

#     return finger_count, finger_tips

# # Initialize video capture
# cap = cv2.VideoCapture(0)

# # Initialize mediapipe hands module
# drawing = mp.solutions.drawing_utils
# hands = mp.solutions.hands
# hand_obj = hands.Hands(max_num_hands=1)

# prev_finger_count = -1
# prev_fingertip_distance = 0
# start_time = 0
# task_text = ""  # Initialize task text

# while True:
#     end_time = time.time()
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)

#     # Process the frame with MediaPipe hands
#     results = hand_obj.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

#     if results.multi_hand_landmarks:
#         hand_landmarks = results.multi_hand_landmarks[0]
#         finger_count, finger_tips = track_fingers(hand_landmarks)

#         # Check if two fingers are present
#         if finger_count == 2:
#             current_fingertip_distance = calculate_distance(finger_tips[0], finger_tips[1])

#             # Detect finger drag (up or down)
#             if prev_fingertip_distance > current_fingertip_distance and not start_time:
#                 start_time = time.time()
#                 task_text = "Increasing Volume..."
#             elif prev_fingertip_distance < current_fingertip_distance and not start_time:
#                 start_time = time.time()
#                 task_text = "Decreasing Volume..."

#             # Volume adjustment logic after a hold time (0.2 seconds)
#             if (end_time - start_time) > 0.2:
#                 if task_text == "Increasing Volume...":
#                     pyautogui.press("volumeup")
#                 elif task_text == "Decreasing Volume...":
#                     pyautogui.press("volumedown")
#                 start_time = 0  # Reset timer

#             prev_fingertip_distance = current_fingertip_distance

#         else:
#             prev_fingertip_distance = 0
#             start_time = 0
#             task_text = ""  # Reset task text

#         # Draw hand landmarks and task text
#         drawing.draw_landmarks(frame, hand_landmarks, hands.HAND_CONNECTIONS)
#         cv2.rectangle(frame, (10, 10), (300, 60), (0, 0, 0), -1)  # Draw a filled black rectangle
#         cv2.putText(frame, task_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

#     cv2.imshow("window", frame)

#     # Check if 'Q' key is pressed to quit
#     key = cv2.waitKey(1)
#     if key == ord('q') or key == 27:  # 'q' or ESC key
#         break

# cv2.destroyAllWindows()
# cap.release()




# import cv2
# import mediapipe as mp
# import pyautogui
# import time

# # Function to count the number of fingers based on landmark positions
# def count_fingers(lst):
#     count = 0

#     threshold = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

#     if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > threshold:
#         count += 1

#     if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > threshold:
#         count += 1

#     if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > threshold:
#         count += 1

#     if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > threshold:
#         count += 1

#     if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
#         count += 1

#     return count

# # Initialize video capture
# cap = cv2.VideoCapture(0)

# # Initialize mediapipe hands module
# drawing = mp.solutions.drawing_utils
# hands = mp.solutions.hands
# hand_obj = hands.Hands(max_num_hands=1)

# start_init = False
# prev = -1

# task_text = ""  # Initialize task text

# while True:
#     end_time = time.time()
#     _, frm = cap.read()
#     frm = cv2.flip(frm, 1)

#     # Process the frame with mediapipe hands
#     res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

#     if res.multi_hand_landmarks:
#         hand_keyPoints = res.multi_hand_landmarks[0]
#         finger_count = count_fingers(hand_keyPoints)

#         if not(prev == finger_count):
#             if not(start_init):
#                 start_time = time.time()
#                 start_init = True
#             elif (end_time - start_time) > 0.2:
#                 if finger_count == 1:
#                     pyautogui.press("right")  # Press right arrow key for forward skip
#                     task_text = "Forward Skip"
#                 elif finger_count == 2:
#                     pyautogui.press("left")  # Press left arrow key for backward skip
#                     task_text = "Backward Skip"
#                 elif finger_count == 3:
#                     pyautogui.press("volumeup")  # Press volume up key for increasing volume
#                     task_text = "Volume Up"
#                 elif finger_count == 4:
#                     pyautogui.press("volumedown")  # Press volume down key for decreasing volume
#                     task_text = "Volume Down"
#                 elif finger_count == 5:
#                     pyautogui.press("space")  # Press spacebar for pause/play
#                     task_text = "Pause/Play"

#                 prev = finger_count
#                 start_init = False

#         drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

#     # Draw task text inside a box
#     cv2.rectangle(frm, (10, 10), (300, 60), (0, 0, 0), -1)  # Draw a filled black rectangle
#     cv2.putText(frm, task_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

#     cv2.imshow("window", frm)

#     if cv2.waitKey(1) == 27:
#         cv2.destroyAllWindows()
#         cap.release()
#         break
















import cv2
import mediapipe as mp
import pyautogui
import time

# Function to check if two fingers are dragged up or down
def check_drag_direction(start_y, end_y):
    if start_y - end_y > 20:  # If fingers move up
        return "up"
    elif end_y - start_y > 20:  # If fingers move down
        return "down"
    else:
        return "none"

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize mediapipe hands module
drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

start_init = False
start_y = None
task_text = ""  # Initialize task text

while True:
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)

    # Process the frame with mediapipe hands
    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:
        hand_keyPoints = res.multi_hand_landmarks[0]

        # Get y-coordinates of index and middle finger tips
        index_finger_y = hand_keyPoints.landmark[8].y * 100
        middle_finger_y = hand_keyPoints.landmark[12].y * 100

        if start_y is None:  # Initialize start_y with the first detected position
            start_y = (index_finger_y + middle_finger_y) / 2

        end_y = (index_finger_y + middle_finger_y) / 2

        if start_init is False:
            start_time = time.time()
            start_init = True
        else:
            # Check direction of finger movement
            direction = check_drag_direction(start_y, end_y)
            if direction == "up":
                pyautogui.press("volumeup")  # Increase volume
                task_text = "Volume Up"
            elif direction == "down":
                pyautogui.press("volumedown")  # Decrease volume
                task_text = "Volume Down"
            
            start_y = end_y  # Update start_y to the new position for continuous tracking

        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

    # Draw task text inside a box
    cv2.rectangle(frm, (10, 10), (300, 60), (0, 0, 0), -1)  # Draw a filled black rectangle
    cv2.putText(frm, task_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("window", frm)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
