import explorerhat
import time
import random


inputBtns = ""
pattern = ""

def button_pressed(channel, event):
    global inputBtns
    
    if channel == 1:
        inputBtns += "1"
        
    elif channel == 2:
        inputBtns += "2"
        
    elif channel == 3:
        inputBtns += "3"

    elif channel == 4:
        inputBtns += "4"
        



explorerhat.touch.pressed(button_pressed)
input("press enter to exit \n")

