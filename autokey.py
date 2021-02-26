# from tkinter import *

# # 宣告
# form = Tk()

# # 視窗標題
# form.title('Demo')
# # 視窗的背景顏色
# form.configure(background='black')
# form.configure(background='#888888')
# # 視窗初始大小
# form.geometry('800x600+0+0')
# # 視窗[左右, 上下]是否可拉大拉小，若都為0則視窗右上角的最大化按鈕會無法點擊
# form.resizable(0, 1)
# # 視窗最大/最小可接受的寬度與高度
# form.minsize(300, 200)
# form.maxsize(600, 400)
# # 自動刷新畫面
# form.mainloop()

from pynput.keyboard import Listener
import pynput
import time,os,signal,threading
import pyautogui
import pydirectinput

def on_press(key):
    pass

def on_release(key):
    all_key.append(str(key))
    # print(all_key)
    delaytime = 0.01
    if "'w'" in all_key:
        # print("開場技能")
        pydirectinput.press('`')
        time.sleep(delaytime)
        pydirectinput.press('5')
        time.sleep(delaytime)
        pydirectinput.press('h')
        time.sleep(delaytime)        
        pydirectinput.press('2')
        time.sleep(delaytime)
        pydirectinput.press('r')
        time.sleep(delaytime)
        pydirectinput.press('3')
        time.sleep(delaytime)
        pydirectinput.press('r')
        time.sleep(delaytime)
        pydirectinput.press('1')
        time.sleep(delaytime)
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('g')
        time.sleep(delaytime)
        pydirectinput.press('t')   
        pydirectinput.keyUp('ctrl')
        time.sleep(delaytime)                       
        all_key.clear()
    if "'e'" in all_key:
        # print("攻擊技能組")
        pydirectinput.press('`')
        time.sleep(delaytime)
        pydirectinput.press('8')
        time.sleep(delaytime)
        pydirectinput.press('r')
        time.sleep(delaytime)
        pydirectinput.press('7')
        time.sleep(delaytime)
        pydirectinput.press('r')
        time.sleep(delaytime)
        pydirectinput.press('6')
        time.sleep(delaytime)
        pydirectinput.press('r')
        time.sleep(delaytime)     
        pydirectinput.press('4')
        time.sleep(delaytime)
        pydirectinput.press('r')
        time.sleep(delaytime)               
        all_key.clear()
    # if "'q'" in all_key:
    #     print("快速離場")
    #     all_key.clear()

    if 'Key.caps_lock' in all_key:
        print("中斷程式")
        return False
    try:
        if all_key[-1] == 'Key.ctrl_l':
            time1 = time.time()
            while True:
                if time.time() - time1 >= 1:
                    all_key.clear()
                    break
    except:
        pass
def start_listen():
    with Listener(on_press=None, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    all_key = []
    start_listen()