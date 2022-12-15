import pyautogui
import time
import os

try:
    def bot():
        pyautogui.alert('Não mexa em nada durante a execução', '                             ',
                        'By: João Pedro Costa Santos')
        pyautogui.PAUSE = 0.5

        os.startfile(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')  # abre o edge
        os.startfile(r'C:\Program Files (x86)\Microsoft Office/root\Office16\OUTLOOK.EXE')  # abre o outlook
        os.startfile(r'C:\Users\marcos.dourado\Desktop\baretail.exe')


    def pos():
        pyautogui.alert('Não mexa em nada durante a execução', '                             ',
                        'By: João Pedro Costa Santos')
        pyautogui.PAUSE = 0.5
        print(pyautogui.position())


    bot()
    time.sleep(5)
    pyautogui.alert('Foi finalizado!', '                             ',
                        'By: João Pedro Costa Santos')
except Exception as e:
    print(e)
    time.sleep(20)
