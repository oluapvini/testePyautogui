#funcao que da o tamanho da resolução da tela
"""print(pyautogui.size())"""

#retorna true ou false se a coordenada estiver dentro da resolução atual
"""print(pyautogui.onScreen(1000, 800))"""

#leva o cursor do mouse as coordenadas indicadas
"""pyautogui.moveTo(720, 450, duration=0)"""

#move o cursor apartir da sua posição relativa
"""pyautogui.moveRel(100, -150, duration=2)"""

#seleciona com o cursor a area da codernada
"""pyautogui.dragTo(100, 200, duration=3)"""

#seleciona com o cursor a area da cordenada a partir da sua posicao relativa
"""pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)"""


#clica no local da coordenada do cursor
"""
pyautogui.click(a, b, clicks=1, interval=0, button='left')
pyautogui.click(a, b, clicks=1, interval=0, button='right')
pyautogui.click(a, b, clicks=1, interval=0, button='midle')
>>> pyautogui.rightClick(x=moveToX, y=moveToY)
>>> pyautogui.middleClick(x=moveToX, y=moveToY)
>>> pyautogui.doubleClick(x=moveToX, y=moveToY)
>>> pyautogui.tripleClick(x=moveToX, y=moveToY)
"""

#define a rolagem do scroll, negativo pra baixo, positivo pra baixo (precisa do middle click)
"""pyautogui.scroll(-1000, x=200, y=200)
>>> pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
>>> pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')"""