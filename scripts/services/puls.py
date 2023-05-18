#!/usr/bin/python3
import os
import time
import xbmc
import xbmcgui

home = xbmcgui.Window(10000)
skin = home.getProperty("CurrentSkin")
puls = (":")
zero = (" ")



while True:
    xbmcgui.Window(10000).setProperty('Puls', puls)
    time.sleep(1)
    xbmcgui.Window(10000).setProperty('Puls', zero)
    time.sleep(1)