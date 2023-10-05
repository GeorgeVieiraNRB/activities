#  G.A.M. (Guides_Auto_Manager)
## "gravar" tela e salvar guias do navegador em alguma estrutura de dados
## salvar informações chave em um .txt para uso futuro
## acessar de alguma forma as informações do monitor
## organizar em termos de Orientação a objetos
## fazer interface
## opçoes de deletar guias nao utilizadas

import pyautogui 
import time
import pygetwindow 
from screeninfo import get_monitors

web_browser=""
SAFE_COEFICIENT=12
monitor = get_monitors()[0]
print(monitor.height)

one_hour = 1
one_minute = 1/100
one_second = 1/1000

def current_guide():
    window = pygetwindow.getActiveWindow()
    window_title= window.title if window != None else ""
    return window_title
initial_window="Visual Studio Code"#window_actual()
def verify_current_window(window):
    return window in current_guide()     
def calculate_time(hour=0,min=0,sec=0):
    return hour*one_hour+min*one_minute+sec*one_second
def calculate_now():
    return calculate_time(time.localtime().tm_hour,time.localtime().tm_min,time.localtime().tm_sec)

window=current_guide()
if "Visual Studio Code" in window:
    pyautogui.hotkey("alt","tab")
now = calculate_now()
print(now)
guides=[]
guides_times=[]
try:
    browser=current_guide()[current_guide().index("-")+1:].replace(" ","")
    print(browser)
except:
    pass
while(calculate_now()-now<5*(1/1000)):
    window=current_guide()
    if(window not in guides):
        guides.append(window)
        guides_times.append(1)

    index=guides.index(window)
    if(current_guide()!=window):
        pass
    guides_times[index]+=1
pyautogui.alert("O código foi finalizado. Você já pode utilizar o computador!")
print("ended")
pyautogui.hotkey("alt","tab")
print("guias"+str(guides))
print("tempos"+str(guides_times))

quantidade_guias = len(guides)
less_used_guides_times=guides[: ]
less_used_guides_times.sort()
less_used_guides_times=less_used_guides_times[:quantidade_guias//2]
less_used_guides=[]
print(less_used_guides_times)
for x,y in enumerate(guides):
    if(guides_times[x] in less_used_guides_times):
        less_used_guides.append(y)
print("guias menos usadas"+str(less_used_guides))

# pyautogui.PAUSE = 0.5
time.sleep(2)
if "Visual Studio Code" in window:
    pyautogui.hotkey("alt","tab")
# Reorganização
for x in range(quantidade_guias*2):
    guide=current_guide()
    pyautogui.PAUSE = 0.5
    time.sleep(1)
    if(guide in less_used_guides):
        pyautogui.hotkey("ctrl","w")
        print(f'{current_guide} foi deletada')
    if(x<quantidade_guias):
        pyautogui.hotkey("ctrl","tab")
    else:
        pyautogui.hotkey("ctrl","shift","tab")
pyautogui.hotkey("alt","tab")
pyautogui.alert("O código foi finalizado. Você já pode utilizar o computador!")
print("ended")
# pyautogui.moveTo(8,5)
# #time.sleep(1)
# pyautogui.mouseDown()#segurar

# pyautogui.mouseUp()#soltar 
# #time.sleep(5)

