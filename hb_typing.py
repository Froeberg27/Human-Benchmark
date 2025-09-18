import numpy as np
import pyautogui
import time
import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("Open the typing game, project starts in 5 seconds")
time.sleep(5)  # click into the game

x,y,w,h = 360, 470, 1200, 310

def get_frame():
    # Take screenshot of region
    frame = pyautogui.screenshot(region=(x, y, w, h))
    # Optionally save for debugging
    frame.save("screenshots/scanned_typing.jpg")
    return frame

frame = get_frame()

# Convert PIL image (from pyautogui) → OpenCV
frame_to_send = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)

# Convert to grayscale
gray_scale = cv2.cvtColor(frame_to_send, cv2.COLOR_BGR2GRAY)

# Threshold for better OCR
_, threshold = cv2.threshold(gray_scale, 150, 255, cv2.THRESH_BINARY_INV)

custom_config = f'--oem 3 --psm 6'
text = pytesseract.image_to_string(threshold, config=custom_config)
print(text)
corrections = {
    "|": "I",    # pipe → capital I
    "\n": " ",  # ENTER (newline) → space
}

for wrong, right in corrections.items():
    text = text.replace(wrong, right)

print("Detected text:", text.strip())

pyautogui.click(920,650)

pyautogui.write(text)
#for k in text:
#    pyautogui.write(k)
#    time.sleep(0.05)