#! /usr/bin/env python
#! coding:utf-8

import pyautogui
import time
import numpy
from idleTime import idle

class PreventScreensaver:
    def __init__(self, start_prevent):
        self.is_idle = False
        self.start = start_prevent

    def detect_idle(self, duration=180):
        dur = idle.get_idle_duration()
        time.sleep(duration)
        print(dur)
        if dur >= duration-5:
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

    def surveillance_loop(self, duration=180):
        try:
            while self.start:
                self.detect_idle(duration=duration)
                if self.is_idle:
                    self.move_cursor()
                    self.volume_control()
                    self.is_idle = False
        except KeyboardInterrupt:
            print("finish")

if __name__ == "__main__":
    ps = PreventScreensaver(start_prevent=True)
    ps.surveillance_loop(5)
