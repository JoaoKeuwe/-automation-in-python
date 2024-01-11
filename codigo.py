import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"    

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2)
pyautogui.click(x=1476, y=463)

pyautogui.write("joaov.ojo@gmail.com")
pyautogui.press("tab")
pyautogui.write("keuwe")
pyautogui.press("enter")

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=1487, y=319)

    pyautogui.write("MOLO000251")
    pyautogui.press("tab")

    pyautogui.write("Logitech")
    pyautogui.press("tab")

    pyautogui.write('notebook')
    pyautogui.press("tab")