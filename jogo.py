import pyautogui
import time
try:
    def bot():
        pyautogui.alert('Não mexa em nada durante a execução')
        pyautogui.PAUSE = 0.5

        pyautogui.hotkey('winleft', '3')  # abre o blitz
        pyautogui.hotkey('winleft')  # abre o skype
        pyautogui.write('League of Legends')  # abre o lol
        pyautogui.hotkey('enter')
        pyautogui.hotkey('winleft', '2')  # abre o spotify
        pyautogui.hotkey('winleft', '6')  # abre o acces
        time.sleep(5)
        pyautogui.click(x=438, y=513)
        pyautogui.hotkey('winleft', '5')  # abre o banco de dados
        pyautogui.click(x=855, y=1044)  # abre os logs

    def pos():
        pyautogui.alert('Não mexa em nada durante a execução')
        pyautogui.PAUSE = 0.5
        print(pyautogui.position())

    bot()
    time.sleep(10)
    pyautogui.alert('Foi finalizado')
except Exception as e:
    print(e)
    time.sleep(20)
