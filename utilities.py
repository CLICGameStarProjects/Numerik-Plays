import subprocess as sp
import time
from pynput.keyboard import Key

def translate(vote):
    return


def switchToWindow(pid):
    string = "wmctrl -ia $(wmctrl -lp | awk -vpid=%s '$3==pid {print $1; exit}')" % (pid)
    #sp.Popen(string, shell=True, stdout=sp.PIPE)
    sp.Popen(string, shell=True)

def launchMenu(pid, kbd):
    switchToWindow(pid)
    time.sleep(0.1)
    kbd.press(Key.enter)
    time.sleep(0.1)
    kbd.release(Key.enter)
    print("Pressed enter")

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

def press_key(pid, kbd, input):
    switchToWindow(pid)
    time.sleep(0.05)
    kbd.press(input)
    time.sleep(0.2)
    kbd.release(input)


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
