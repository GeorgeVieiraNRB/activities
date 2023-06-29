#  G.A.M. (Guides_Auto_Manager)
## calcular o tamanho de uma guia - ok
## "gravar" tela e salvar localizações do mouse em alguma estrutura de dados
## selecionar as localizações do mouse relativas as guias
## mover as guias mais usadas para o canto esquerdo
## adaptar codigo para servir em qualquer tela
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

def current_window():
    window = pygetwindow.getActiveWindow()
    window_title= window.title if window != None else ""
    print("Programa em execução:", window_title)
    return window_title
initial_window="Visual Studio Code"#window_actual()
def verify_current_window(window):
    return window in current_window()     
def calculate_time(hour=0,min=0,sec=0):
    return hour*1+min*0.01+sec*0.0001
def calculate_now():
    return calculate_time(time.localtime().tm_hour,time.localtime().tm_min,time.localtime().tm_sec)
def calculate_distance(now_time,end_time,start_location=0):
    print("1")
    #web_browser=current_window()
    #while verify_current_window(initial_window):
    
        
    pyautogui.moveTo(start_location+SAFE_COEFICIENT,SAFE_COEFICIENT)
    mouse_y_positions=mouse_x_positions=[]
    
    #time.sleep(1)
    while now_time < end_time:
        now_time=calculate_now() 
        x1,y1 = pyautogui.position()
        mouse_x_positions.append(x1)
        mouse_y_positions.append(y1)
    mouse_x_positions.sort()
    min_x=mouse_x_positions[0]
    max_x=mouse_x_positions[-1]
    mouse_y_positions.sort()
    min_y=mouse_x_positions[0]
    max_y=mouse_x_positions[-1]
    #time.sleep(1)
    #while not verify_current_window(initial_window) or verify_current_window(web_browser):
    #print("a")
    pyautogui.PAUSE = 1
    #pyautogui.hotkey("alt","tab")
    pyautogui.PAUSE = 0.5
    return max_x-min_x,max_y-min_y

window=current_window()
if "Visual Studio Code" in window:
    pyautogui.hotkey("alt","tab")
now = calculate_now()
pyautogui.alert("A calibração do sistema vai começar, primeiro mova o mouse entre o canto esquerdo da tela e o final do espaço antes da primeira guia")

space_before_guide= calculate_distance(now,now+calculate_time(sec=10))[0]+SAFE_COEFICIENT
print(f'space_before_guide:{space_before_guide}')
#time.sleep(2)
pyautogui.alert("Agora mova o mouse entre o começo e o final da primeira guia")
pyautogui.PAUSE = 0.5
guide_x_size,guide_y_size = calculate_distance(now,now+calculate_time(sec=20),start_location=100)
print(f'guide_size:{guide_x_size}')
#time.sleep(2)
def clicks_locations():
    mouse_positions=[] 
    limit_time = now + calculate_time(sec=5)
    print(f"now {now} limit_time {limit_time}")
    print("running...") 
    while now < limit_time:
        x,y = pyautogui.position()#coordenadas atuais do mouse
        mouse_positions.append((x,y))
        now = calculate_now()
        #print(f"{x} {y}")
        #print(f"now {now} limit_time {limit_time}")

    print(f"now {now} limit_time {limit_time}")
    print(mouse_positions)
pyautogui.alert("Etapa de organização de guias , não toque no mouse")
print("running")

pyautogui.PAUSE = 1
#pyautogui.hotkey("alt","tab")

time.sleep(1)
#pyautogui.hotkey("alt","tab")

pyautogui.moveTo((guide_x_size//3)+space_before_guide,5)
#time.sleep(1)
pyautogui.mouseDown()#segurar
pyautogui.moveTo(int(guide_x_size*1.2)+space_before_guide,5)
pyautogui.mouseUp()#soltar 
#time.sleep(5)

pyautogui.alert("O código foi finalizado. Você já pode utilizar o computador!")
print("ended")