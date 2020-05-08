#! /usr/bin/env python
#! coding:utf-8

import pyautogui
import time
import numpy
from idleTime import idle

is_idle = False

def detect_idle(duration=180):
    global is_idle
    dur = idle.get_idle_duration()
    time.sleep(duration)
    # print(dur)
    if dur >= duration-5:
        # print("idle detected")
        is_idle = True
    else:
        # print("not idle state")
        is_idle = False

def move_cursor():
    global is_idle
    pyautogui.move(-100,0,duration=1.0)
    time.sleep(2.0)
    pyautogui.move(100,0,duration=1.0)
    is_idle = False

if __name__ == "__main__":
    try:
        while True:
            detect_idle()
            if is_idle:
                move_cursor()
    except KeyboardInterrupt:
        print("finish")