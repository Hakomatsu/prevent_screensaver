#! /usr/bin/env python
#! coding:utf-8

import pyautogui
import time
import numpy
from idleTime import idle

class PreventScreensaver:
    def __init__(self):
        self.is_idle = False
        self.start = False
        self.duration = 180

    def set_start_flag(self, flag):
        self.start = flag

    def set_duration(self, duration):
        self.duration = duration

    def detect_idle(self):
        dur = idle.get_idle_duration()
        time.sleep(self.duration)
        print(dur)
        if dur >= self.duration-5:
            print("idle detected")
            self.is_idle = True
        else:
            print("not idle state")
            self.is_idle = False

    def move_cursor(self):
        for i in range(10):
            pyautogui.move(-100,0,duration=0.1)
            pyautogui.move(100,0,duration=0.1)

    def volume_control(self):
        pyautogui.press("volumedown", presses=5)
        time.sleep(1)
        pyautogui.press("volumeup", presses=5)
        time.sleep(1)

    def surveillance_loop(self):
        try:
            while True:
                self.detect_idle()
                if self.is_idle:
                    self.move_cursor()
                    self.volume_control()
                    self.is_idle = False
        except KeyboardInterrupt:
            print("finish")

    def surveillance(self):
        try:
            self.detect_idle()
            if self.is_idle:
                self.move_cursor()
                self.volume_control()
                self.is_idle = False
        except KeyboardInterrupt:
            print("finish")
   
"""   
if __name__ == "__main__":
    ps = PreventScreensaver()
    ps.set_duration(5)
    ps.surveillance_loop()
"""