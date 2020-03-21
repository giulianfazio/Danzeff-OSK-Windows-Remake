from kivy.core.window import Window
from KivyOnTop import register_topmost

import win32gui
import win32con
import win32api

'''
The Implementation of this file is OS specific and at the moment only Windows is supported
'''


def set_always_upront(window_title):
    register_topmost(Window, window_title)

def set_transparency(window_title, transparency_level):
    handle = win32gui.FindWindow(None, window_title)
    win32gui.SetWindowLong(handle, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(handle, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(handle, win32api.RGB(0, 0, 0), 210, win32con.LWA_ALPHA)