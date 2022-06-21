# Importações Bibliotecas

import pyautogui
import time

# Perguntar quantos XML no dia

Nxml = 0
TotalXML = int (input ("Quantos XML temos hoje?"))
pyautogui.PAUSE = 1 # Tempo de delay Global(pode ser alterado)

# Entrar no site da Fazenda

pyautogui.hotkey ("ctrl","t") # Abrir uma nova aba 
pyautogui.click (x=638, y=85)
pyautogui.write ("https://www.nfe.fazenda.gov.br")
pyautogui.press ("enter")
time.sleep(1.5)
pyautogui.click (x=1102, y=370)
pyautogui.press("tab")
pyautogui.press("enter") #Nova Consulta
pyautogui.click(x=910, y=586)
pyautogui.press("tab")
pyautogui.press("enter") #Consulta NF
pyautogui.click(x=1146, y=637)
pyautogui.press("tab") #Codigo 

#Entrar No Word Lista de xml

pyautogui.hotkey ("win", "s")
pyautogui.write ("XML")
pyautogui.press ("enter")
time.sleep (6)

# Download Primeiro XML ( Certificado )

pyautogui.click (x=430, y=424) 
pyautogui.hotkey ("ctrl", "x") # Recortar o Primeiro XML do Word
pyautogui.keyDown ("alt") # Presionar tecla Alt
pyautogui.press ("tab") # Clicar TAB
pyautogui.keyUp ("alt") # Soltar tecla Alt
pyautogui.hotkey ("ctrl", "v") # Colar XML
pyautogui.press("tab")
pyautogui.press("enter")#Captcha
pyautogui.press("tab",presses = 4,interval=0.1)#Confirmar
pyautogui.press("enter")
pyautogui.click(x=746, y=655)
pyautogui.keyDown ("shift")
pyautogui.press("tab",presses = 2, interval = 0.1)
pyautogui.keyUp ("shift")
pyautogui.press("enter",presses = 2, interval = 1)#Download
#POP UP CERTIFICADO
pyautogui.click (x=1102, y=370)
pyautogui.press("tab")#Prepara o Proximo
pyautogui.press("enter") #Nova Consulta
pyautogui.click(x=910, y=586)
pyautogui.press("tab")
pyautogui.press("enter") #Consulta NF
pyautogui.click(x=1146, y=637)
pyautogui.press("tab") #Codigo 
Nxml = Nxml + 1

# Loop para demais Downloads

while Nxml < TotalXML: 
    pyautogui.keyDown ("alt") # Presionar tecla Alt
    pyautogui.press ("tab") # Clicar TAB
    pyautogui.keyUp ("alt") # Soltar tecla Alt
    pyautogui.click (x=430, y=424) 
    pyautogui.hotkey ("ctrl", "x") # Recortar o Primeiro XML do Word
    pyautogui.keyDown ("alt") # Presionar tecla Alt
    pyautogui.press ("tab") # Clicar TAB
    pyautogui.keyUp ("alt") # Soltar tecla Alt
    pyautogui.hotkey ("ctrl", "v") # Colar XML
    pyautogui.press("tab")
    pyautogui.press("enter")#Captcha
    pyautogui.press("tab",presses = 4,interval=0.1)#Confirmar
    pyautogui.press("enter")
    pyautogui.click(x=746, y=655)
    pyautogui.keyDown ("shift")
    pyautogui.press("tab",presses = 2, interval = 0.1)
    pyautogui.keyUp ("shift")
    pyautogui.press("enter",presses = 2, interval = 1)#Download
    #POPUP CERTIFICADO
    pyautogui.click (x=1102, y=370)
    pyautogui.press("tab")#Prepara o Proximo
    pyautogui.press("enter") #Nova Consulta
    pyautogui.click(x=910, y=586)
    pyautogui.press("tab")
    pyautogui.press("enter") #Consulta NF
    pyautogui.click(x=1146, y=637)
    pyautogui.press("tab") #Codigo 
    Nxml = Nxml + 1
