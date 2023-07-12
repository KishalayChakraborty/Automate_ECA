import pyautogui
import win32gui
import time
#pyautogui.PAUSE = 
pyautogui.FAILSAFE = True
 


startLoc=[]
winLoc=[]
def getLocs(window_title):
    global startLoc,winLoc
    hwnd = win32gui.FindWindow(None, window_title) 
    left, top, _, _ = win32gui.GetClientRect(hwnd)
    window_left, window_top = win32gui.ClientToScreen(hwnd, (left, top))
    winLoc=[window_left, window_top]
    
    startLoc = pyautogui.locateOnScreen('start.png', confidence=0.9)

def changeFN(fn):
    pyautogui.click(startLoc.left+250, startLoc.top+20)
    pyautogui.click(startLoc.left+250, startLoc.top+20)
    pyautogui.press('left', presses=10)   
    pyautogui.press('del', presses=30)  
    pyautogui.write(fn) 
    pyautogui.click(startLoc.left+450, startLoc.top+20)#set btn


def selectDPV():
    #pyautogui.moveTo(winLoc[0]+160, winLoc[0]+70, duration=1)#dpvTab
    pyautogui.click(winLoc[0]+160, winLoc[0]+70)#dpvTab
 
def startExp():
    pyautogui.moveTo(startLoc.left+20, startLoc.top+20, duration=1)#start btn
    #pyautogui.click(startLoc.left+20, startLoc.top+20)

def move_mouse_to_top_left(window_title):
    # Find the window by title
    hwnd = win32gui.FindWindow(None, window_title)
    
    # Get the window's left and top position
    left, top, _, _ = win32gui.GetClientRect(hwnd)
    window_left, window_top = win32gui.ClientToScreen(hwnd, (left, top))
    
    # Move the mouse to the top left corner of the window
    pyautogui.moveTo(window_left, window_top, duration=1)
    b = pyautogui.locateOnScreen('start.png', confidence=0.9)
    
    #pyautogui.moveTo(b.left+20, b.top+20, duration=1)#start btn
    #pyautogui.moveTo(b.left+250, b.top+20, duration=1)#Filename
    pyautogui.click(b.left+250, b.top+20)
    pyautogui.click(b.left+250, b.top+20)
    pyautogui.press('left', presses=10)   
    pyautogui.press('del', presses=30)  
    pyautogui.write('Helloworld') 
    pyautogui.click(b.left+450, b.top+20)#set btn
    
    print(b)
# Main function
def main():
    window_title = "KME Stat"  # Replace with the actual title of the window
    
    # Move the mouse to the top left corner of the window
    getLocs(window_title)
    selectDPV()
    changeFN("filenametesting")
    for i in range(0,10):
        startExp()
        time.sleep()
    
if __name__ == '__main__':
    main()
