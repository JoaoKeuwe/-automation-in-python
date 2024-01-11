import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.5

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
    pyautogui.click(x=1503, y=328)
    pyautogui.click()
    
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
        
    pyautogui.press("tab")
    pyautogui.press("enter")    
    