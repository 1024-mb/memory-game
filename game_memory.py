import explorerhat
import time
import random


patternInpt = []
patternPI = []
patternLength=4


def check_pattern():
    global patternInpt, patternPI, patternLength
    outInp = ""
    outPI = ""
    matches = 0
    
    for i in range(0, len(patternInpt)):
        outInp += str(patternInpt[i])
        outPI += " "
        outPI += str(patternPI[i])
        outInp += " "
        
        if patternInpt[i] == patternPI[i]:
            matches+= 1
        
    print(f"Your Input:   {outInp}")
    print(f"Pattern:   {outPI}")
    matches = int(matches/len(patternInpt) * 100)
    print(f"Percentage Match: {matches}\n")

    if (patternInpt == patternPI):
        print("Press enter to continue to the next level." )
        patternLength+=1
        patternInpt = []
        patternPI = []
        
    else:
        print("Wrong!")


def light_show():
    explorerhat.light[0].on()
    time.sleep(0.07)
    explorerhat.light[0].off()
    explorerhat.light[1].on()
    time.sleep(0.07)
    explorerhat.light[1].off()
    explorerhat.light[2].on()
    time.sleep(0.07)
    explorerhat.light[2].off()
    explorerhat.light[3].on()
    time.sleep(0.1)
    explorerhat.light[3].off()
    explorerhat.light[2].on()
    time.sleep(0.07)
    explorerhat.light[2].off()    
    explorerhat.light[1].on()
    time.sleep(0.07)
    explorerhat.light[1].off()    
    explorerhat.light[0].on()
    time.sleep(0.07)
    explorerhat.light[0].off()


def button_pressed(channel, event):
    global patternInpt, patternPI, patternLength
    
    if(len(patternPI) == patternLength):
        if len(patternPI) > len(patternInpt):
            explorerhat.light[channel - 1].on()
            time.sleep(0.3)
            explorerhat.light[channel - 1].off()

            if channel == 1:
                patternInpt.append(0)
                
            elif channel == 2:
                patternInpt.append(1)
                
            elif channel == 3:
                patternInpt.append(2)

            elif channel == 4:
                patternInpt.append(3)
            

        
def add_values():
    global patternPI, patternLength
    for i in range(0, patternLength):
        selectedButton = random.randint(0, 3)
        
        if(not(len(patternPI) == 0)):
            while (patternPI[len(patternPI) - 1] == selectedButton):
                selectedButton = random.randint(0, 3)
            
            explorerhat.light[selectedButton].on()
            time.sleep(0.5)
            explorerhat.light[selectedButton].off()
            patternPI.append(selectedButton)

        else:
            patternPI.append(selectedButton)        
            explorerhat.light[selectedButton].on()
            time.sleep(0.5)
            explorerhat.light[selectedButton].off()
            

nextLight = True

def wait_for_input():
    input_timeout = 20
    """Wait for the player to input the correct pattern or timeout."""
    start_time = time.time()  # Record the start time
    while len(patternInpt) < patternLength:
        # Check if time has exceeded the input timeout
        if time.time() - start_time > input_timeout:
            print("Time's up! You took too long.")
            check_pattern()  # Proceed with checking the pattern (may indicate failure)
            return False  # Timeout occurred, return False
        time.sleep(0.1)  # Small delay to prevent high CPU usage during the wait

    return True  # If the pattern is completed before timeout

while nextLight==True:
    nextLight = False
    
    for i in range(5):
        light_show()

    time.sleep(0.7)

    add_values()
    print("\nEnter Pattern With Keypads")
    
    explorerhat.touch.pressed(button_pressed)

    if not wait_for_input():
        print("Moving to next round...")
        continue  # Skip to the next round if the player timed out

    check_pattern()

    patternPI = []
    patternInpt = []

    r = input("Press enter to continue, Q to exit \n")
    
    if r=="Q":
        exit()
        
    else:
        nextLight = True
    


    