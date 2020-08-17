import pyautogui
size=pyautogui.size()[0]
print(size)

def a(ex,ey,x,y):
    ex=int(ex)
    ey=int(ey)
    x=int(x)
    y=int(y)

    if ex<x:
        l=abs(ex-x)
        print('右移',l)
        pyautogui.moveRel(l,0,duration=0.25)
    
    if ex>x:
        l=abs(ex-x)
        print('左移',l)
        pyautogui.moveRel(-l,0,duration=0.25)
    if ey>y:
        l=abs(ey-y)
        print('上移',l)
        pyautogui.moveRel(0,-l,duration=0.25)
    if ey<y:
        l=abs(ey-y)
        pyautogui.moveRel(0,l,duration=0.25)

