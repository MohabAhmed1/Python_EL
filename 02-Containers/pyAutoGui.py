import pyautogui
from time import sleep

def delete(s):
    before_delete_pos_x =209
    before_delete_pos_y =146
    pyautogui.moveTo(before_delete_pos_x,before_delete_pos_y )
    pyautogui.click(x=before_delete_pos_x, y=before_delete_pos_y, clicks=1, interval= 1, button='left')
    #delete "clangd" to write another extension
    for _ in range (len(s)):
        pyautogui.typewrite(['backspace'])

def MoveAndClick(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.click(x=x, y=y, clicks=1, interval= 1, button='left')



try:
    location=None
    while location is None:
        location = pyautogui.locateOnScreen('Menu.png',confidence =0.9)
        sleep(2)
        MoveAndClick(location.left,location.top)
        pyautogui.typewrite('vs')
        
    sleep(0.5)
    vs_icon_x=616
    vs_icon_y=187
    MoveAndClick(vs_icon_x,vs_icon_y)

    ########################################
    sleep(4)
    location = None
    while location is None:
        #Press on Extension icon 
        location = pyautogui.locateOnScreen('sr.png',confidence =0.9)
        sleep(0.5)
    MoveAndClick(location.left,location.top)

    ########################################

    #Move to search bar and typing clangd
    sleep(0.5)
    search_bar_x = 209
    search_bar_y = 146
    MoveAndClick(search_bar_x,search_bar_y)
    pyautogui.typewrite('clangd', interval=0.5)

    ########################################

    # downloading clangd
    sleep(1)
    install_x =269
    install_y =226
    MoveAndClick( install_x , install_y )
    sleep(0.5)
    delete('langd')
    ########################################

    # typing c++ testmate
    sleep(0.5)
    MoveAndClick(search_bar_x,search_bar_y)
    pyautogui.typewrite('++ testmate', interval=0.5)
    sleep(2.5)
    #press on install
    MoveAndClick(install_x,install_y)
    sleep(2)
    delete('testmate')

    ########################################

    # typing c++ helper
    sleep(1)
    MoveAndClick(search_bar_x,search_bar_y)
    pyautogui.typewrite('helper', interval=0.5)
    sleep(2)
    #press on install
    MoveAndClick(install_x,install_y)
    sleep(1)
    delete('++ helper')

    ########################################
    # typing cmake helper
    sleep(0.5)
    MoveAndClick(search_bar_x,search_bar_y)
    pyautogui.typewrite('make', interval=0.5)
    sleep(2.5)
    #press on install
    MoveAndClick(install_x,install_y)
    sleep(1)
    #delete('cmake')

    ########################################
    # typing cmake tools
    sleep(0.5)
    MoveAndClick(search_bar_x,search_bar_y)
    pyautogui.typewrite(' tools', interval=0.5)
    sleep(2.8)
    #press on install
    MoveAndClick(install_x,install_y)
    sleep(1)
    delete('cmake tools')


except:
    print("Not found")    

