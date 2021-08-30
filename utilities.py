import subprocess as sp
import time
from pynput.keyboard import Key
import re

#Mourir
def translate(input):
    if input=="a":
        return "x"
    elif input=="b":
        return "c"
    elif input=="up":
        return Key.up
    elif input=="down":
        return Key.down
    elif input=="left":
        return Key.left
    elif input=="right":
        return Key.right
    elif input=="enter":
        return Key.enter
    elif input=="f1":
        return Key.f1
    elif input=="f2":
        return Key.f2   
    elif input=="f3":
        return Key.f3       
    print("Input not recognized")
    return 

# C'est le cadeau pour la régie. L'écran de la régie doit être parfaitement à droite, en 4k. 
# Ces calculs sont faits pour un moniteur principal en quadK.
# 

def resizeAndPlace(pidA, pidD):
    string = "xdotool windowsize $(wmctrl -lp | awk -vpid=%s '$3==pid {print $1; exit}') 1620 1080" % (pidA) #3:2 aspect ratio
    sp.Popen(string, shell=True)
    string = "xdotool windowsize $(wmctrl -lp | awk -vpid=%s '$3==pid {print $1; exit}') 1620 1080" % (pidD)
    sp.Popen(string, shell=True)
    string = "xdotool windowmove $(wmctrl -lp | awk -vpid=%s '$3==pid {print $1; exit}') 2560 0" % (pidA)
    sp.Popen(string, shell=True)
    string = "xdotool windowmove $(wmctrl -lp | awk -vpid=%s '$3==pid {print $1; exit}') 4480 0" % (pidD) #(2560 + 3840/2 = 4480) 
    sp.Popen(string, shell=True)

def switchToWindow(pid):
    print("switching to ",pid)
    #Trivial, le code s'explique par lui même
    string = "wmctrl -ia $(wmctrl -lp | awk -vpid=%s '$3==pid {print $1}')" % (pid)
    sp.Popen(string, shell=True)


#Felt clever, might delete later
def launchMenu(pid, kbd):
    switchToWindow(pid)
    time.sleep(0.1)
    kbd.press(Key.enter)
    time.sleep(0.1)
    kbd.release(Key.enter)
    print("Pressed enter")


#Envoie un input sur les deux fenêtres à la fois, les délais sont assez vitaux malheureusement
def sync_input(pid1, pid2, kbd, input):
    switchToWindow(pid1)
    time.sleep(0.05)
    kbd.press(input)
    time.sleep(0.2)
    kbd.release(input)


    switchToWindow(pid2)
    time.sleep(0.1)
    kbd.press(input)
    time.sleep(0.2)
    kbd.release(input)
#Emule un input sur une seule fenêtre.
def press_key(pid, kbd, input):
    switchToWindow(pid)
    time.sleep(0.05)
    kbd.press(input)
    time.sleep(0.2)
    kbd.release(input)

#Rigolo mais useless
def startRoutine(pid1, pid2, kbd):
    sync_input(pid1, pid2, kbd, Key.enter)
    time.sleep(0.3)
    sync_input(pid1, pid2, kbd, Key.enter)
    time.sleep(0.3)    
    sync_input(pid1, pid2, kbd, Key.enter)
    time.sleep(0.3)
    sync_input(pid1, pid2, kbd, "x")
    time.sleep(6)
    for i in range(100):
        sync_input(pid1, pid2, kbd, "x")
        time.sleep(0.7)


def launch_place_firefox():
    string = "firefox --new-window numerikplays.ch/stats & echo $!"
    terminal2 = sp.Popen(string, shell=True, stdout=sp.PIPE)
    time.sleep(2)
  

    string = 'xdotool search --name "Mozilla Firefox"'
    terminal2 = sp.Popen(string, shell=True, stdout=sp.PIPE)
    lines = [line.rstrip() for line in terminal2.stdout.readlines()]
    widFirefox = re.sub("[^0-9]","", str(lines[-1]))   
    print(widFirefox)


    string = 'xdotool windowsize  %s 3840 1080'% (widFirefox) 
    sp.Popen(string, shell=True)
    
    string = 'xdotool windowmove  %s 2560 1095'% (widFirefox)
    sp.Popen(string, shell=True)

    return widFirefox


def reset_place_firefox(widFirefox):
    print("WID", widFirefox)
    string = 'xdotool windowsize  %s 3840 1080'% (widFirefox) 
    sp.Popen(string, shell=True)
    
    string = 'xdotool windowmove  %s 2560 1095'% (widFirefox)
    sp.Popen(string, shell=True)

def vladi_mir_cache(cache, elem, cache_size):
    if len(cache)<cache_size:
        cache.append(elem)
    else:
        for i in range (1,cache_size-1):
            cache[i-1]=cache[i]
        cache[cache_size-1]=elem
    return cache