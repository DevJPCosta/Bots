
import pyautogui
import time
import os
try:
    def bot ():
        pyautogui.alert('Não mexa em nada durante a execução','                             ',
                        'By: João Pedro Costa Santos')
        pyautogui.PAUSE= 0.5

        pyautogui.hotkey('winleft','7') #abre o Wpp
        pyautogui.hotkey('winleft', '8') #abre o skype
        pyautogui.hotkey('winleft', '9')  # abre o e-mail trab
        pyautogui.hotkey('winleft','4') #abre navegador
        pyautogui.hotkey('winleft', '5')  # abre o banco de dados
        pyautogui.click(x=855, y=1044) #abre os logs
        os.startfile("G:\Access/v2007\João Pedro Santos\Vendas Diaria v2007N JP.accdb") #abre access
        os.startfile("X:\JP\Cópia de Telefonia.xlsx") #abre lista dos ramais


    def pos ():
        pyautogui.alert('Não mexa em nada durante a execução','                             ',
                        'By: João Pedro Costa Santos')
        pyautogui.PAUSE= 0.5
        print (pyautogui.position())

    bot()
    time.sleep(5)
    pyautogui.alert('Foi finalizado')
except Exception as e:
    print(e)
    time.sleep(20)

