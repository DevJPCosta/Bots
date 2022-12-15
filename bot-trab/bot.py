
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
        os.startfile(r'C:\Program Files (x86)\Microsoft Office/root\Office16\OUTLOOK.EXE')   # abre o e-mail trab
        os.startfile(r'C:\Users\joao.santos\AppData\Local\Programs\Opera GX\launcher.exe') #abre navegador
        os.startfile(r'C:\Program Files (x86)\Microsoft SQL Server Management Studio 18\Common7\IDE\Ssms.exe')  # abre o banco de dados
        os.startfile(r'C:\Users\joao.santos\Desktop\baretail.exe')
        os.startfile(r'G:\Access\v2007\João Pedro Santos\Vendas Diaria v2007N JP.accdb') #abre access
        os.startfile(r'X:\JP\Cópia de Telefonia.xlsx') #abre lista dos ramais


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

