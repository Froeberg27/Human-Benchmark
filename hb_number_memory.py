import numpy as np
import pyautogui
import time
import cv2
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = f"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("Open the number memory game, project starts in 5 seconds")
time.sleep(5)  # click into the game

start_button_coords = [920, 720]
submit_button_coords = [920, 650]
x,y,w,h = 400, 450, 1200, 300

def start_or_next_game():
    pyautogui.click(start_button_coords[0], start_button_coords[1])

def submit_button():
    pyautogui.click(submit_button_coords[0], submit_button_coords[1])


def get_frame():

    frame = pyautogui.screenshot("screenshots/scanned_pic6.jpg", region=(x,y,w,h))
    return frame

while True: 
    start_or_next_game()
    time.sleep(0.2)
    frame = get_frame()

    frame_to_send = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)

    gray_scale = cv2.cvtColor(frame_to_send, cv2.COLOR_BGR2GRAY)

    _, threshold = cv2.threshold(gray_scale, 150, 255, cv2.THRESH_BINARY_INV)

    custom_config = f'--oem 3 --psm 6 outputbase digits'
    text = pytesseract.image_to_string(threshold, config=custom_config)

    print("Detected numbers:", text.strip())

    #time.sleep(2)
    # Debug view
    #cv2.imshow("Processed", threshold)
    #cv2.waitKey(0)
    time.sleep(len(text))

    for k in text:
        pyautogui.write(k)
        time.sleep(0.1)

    #pyautogui.write(text.strip())

    time.sleep(2)

    submit_button()

    #time.sleep(len(text))

    #start_or_next_game()

    time.sleep(2)