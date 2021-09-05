# sending unlimited count of messages.
import pyautogui
import time

while True:
    time.sleep(4)
    pyautogui.typewrite('Good morning😊😜❤')
    time.sleep(2)
    pyautogui.press('enter')

# # Limit the number of message that is sent

# message = 5
# while message > 0:
#     time.sleep(4)
#     pyautogui.typewrite('Who are you?')
#     time.sleep(2)
#     pyautogui.press('enter')
