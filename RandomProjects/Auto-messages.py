# sending unlimited count of messages.
import pyautogui, webbrowser
import time
import pywhatkit

# try:
#     pywhatkit.sendwhatmsg("+447934953640", "Mensaje prueba", 19,54)
#     print("Mensaje enviado")
# except: 
#     print("Ocurrio un Error")


# webbrowser.open('https://web.whatsapp.com/send?phone= +447934953640')

for i in range(5):
    time(20)

    pyautogui.typewrite('mensaje de prueba')
    time.sleep(2)
    pyautogui.press('enter')



# message = 5
# while message > 0:
#     time.sleep(4)
#     pyautogui.typewrite('Who are you?')
#     time.sleep(2)
#     pyautogui.press('enter')
