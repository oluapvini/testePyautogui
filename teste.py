import pyautogui

#funcao que tras a posicao atual do mouse
print(pyautogui.position())

a,b = pyautogui.position()

print(a)
print(b)

#minimizando pycharm
pyautogui.click(1319, 14, clicks=1, interval=0, button='left')

#selecionando primeiro valor da conta
pyautogui.click(52, 160, clicks=1, interval=0, button='left')

#digitando primeiro valor
pyautogui.typewrite('2', interval=0.2)

#selecionando segundo valor da conta
pyautogui.click(230, 160, clicks=1, interval=0, button='left')

#digitando segundo valor
pyautogui.typewrite('2', interval=0.2)

#selecionando tipo da conta
pyautogui.click(409, 160, clicks=1, interval=0, button='left')
pyautogui.click(428, 194, clicks=1, interval=0, button='left')

#calculando
pyautogui.click(497, 165, clicks=1, interval=0, button='left')

#copiando informação (valor da conta)
pyautogui.dragTo(9, 104, duration=2)
pyautogui.rightClick(x=9, y=104)
pyautogui.click(26, 110, clicks=1, interval=0, button='left')


