#! /usr/bin/env python
#! coding: utf-8
# Reference: https://qiita.com/toriiico/items/0b26ef583e176eecce5d

import os
import sys
import wx
import wx.adv
import threading
import prevent_screensaver as ps

TRAY_TOOLTIP = "Prevent Screensaver"
TRAY_ICON = "icon.ico"
pso = ps.PreventScreensaver()

def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)
    return item

def prevent_screensaver():
    pso = ps.PreventScreensaver()
    pso.surveillance()

class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.on_start)
        self.Bind(wx.adv.EVT_TASKBAR_RIGHT_DCLICK, self.on_stop)
        self.condition = False
    
    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, "Start", self.on_start)
        menu.AppendSeparator()
        create_menu_item(menu, "Stop", self.on_stop)
        menu.AppendSeparator()
        create_menu_item(menu, "Exit", self.on_exit)
        return menu
    
    def set_icon(self, path):
        icon = wx.Icon(wx.Bitmap(path))
        self.SetIcon(icon, TRAY_TOOLTIP)
    
    def on_prevent_screensaver(self, event):
        prevent_screensaver()
    
    def on_start(self, event):
        global pso
        self.condition = True
        threading.Thread(target=pso.set_flag, args=(self.condition,)).start()
    
    def on_stop(self, event):
        global pso
        self.condition = False
        threading.Thread(target=pso.set_flag, args=(self.condition,)).start()

    def on_exit(self, event):
        self.on_stop(event)
        wx.CallAfter(self.Destroy)
        self.frame.Close()
        print("Exit")

class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        print("Launch App")
        return True
