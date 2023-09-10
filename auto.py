import pyautogui
import time

import os

def sequence(name, duration, click, thres):
    # output to terminal
    print(f"Initiate sequence {name}")
    
    # define the confidence level for image matching
    confidence_threshold = thres

    # define the maximum number of retries
    max_retries = 10

    # boolean to check if program complete successfully
    is_completed = False

    retries = 0  
    while retries < max_retries:
        region = pyautogui.locateOnScreen(f'resources/{name}.png', confidence=confidence_threshold)
        # region = pyautogui.locateOnScreen(os.path.join(os.path.dirname(__file__), 'images', f'{name}.png'), confidence=confidence_threshold)
        
        if region:
            x, y = pyautogui.center(region)
            
            # some sequence requires multiple click
            for i in range(click): 
                pyautogui.click(x, y)
                time.sleep(0.5)
                
            is_completed = True
            break
        else:
            retries += 1
            time.sleep(duration)
       
    # sleep for the duration or it will click too fast     
    time.sleep(duration)
    return is_completed

def auto(duration, wait_time, load_game):    
    sequence('begin', duration, 1, 0.8)
    sequence('select', duration, 1, 0.8)
    sequence('replenish', duration, 1, 0.8)
    sequence('commence', duration, 1, 0.8)
    
    # do this for 4 days
    for i in range(1):
        # there is a screen change
        time.sleep(wait_time)
        
        sequence('skip', duration, 2, 0.6)
        sequence('continue', duration, 1, 0.8)
        pyautogui.press('a')
        time.sleep(duration)
        
        if not sequence('mine', duration, 1, 0.4):
            # try hunting if we couldn't not find any mine spot
            sequence('hunting', duration, 1, 0.4)

    
        # image recognition is hard here, just press mapped keys
        pyautogui.press('r')
        time.sleep(duration)
        pyautogui.press('t')
        time.sleep(duration)
        pyautogui.press('y')
        time.sleep(duration)
        pyautogui.press('u')
        time.sleep(load_game)
        pyautogui.press('i')
        time.sleep(duration)
        pyautogui.press('y')
        time.sleep(wait_time)
        pyautogui.press('y') # press a key to continue
        time.sleep(wait_time)
        
        sequence('mine', duration, 1, 0.4)

        if not sequence('mine', duration, 1, 0.4):
            # try hunting if we couldn't not find any mine spot
            sequence('hunting', duration, 1, 0.4)

            
        # image recognition is hard here, just press mapped keys
        pyautogui.press('r')
        time.sleep(duration)
        pyautogui.press('t')
        time.sleep(duration)
        pyautogui.press('y')
        time.sleep(duration)
        pyautogui.press('u')
        time.sleep(load_game)
        pyautogui.press('i')
        time.sleep(duration)
        pyautogui.press('y')
        time.sleep(wait_time)
        pyautogui.press('y') # press a key to continue
        time.sleep(wait_time)
        
        sequence('advance', duration, 2, 0.6)     
    
    # exit sequence
    sequence('skip', duration, 2, 0.6)
    sequence('continue', duration, 1, 0.8)
    sequence('back', duration, 1, 0.8)
    sequence('abandon', duration, 1, 0.8)
    pyautogui.press('u') # press yes
    time.sleep(wait_time)
    sequence('next', duration, 1, 0.8)
    sequence('confirm', duration, 1, 0.8)
    pyautogui.press('y') # press a key to continue
    time.sleep(duration)


    
    
    
    