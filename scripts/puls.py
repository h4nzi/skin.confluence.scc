#!/usr/bin/python3
# coding=utf-8
import os
import time
import xbmc
import xbmcgui

home = xbmcgui.Window(10000)
skin = home.getProperty("CurrentSkin")
puls = (":")
zero = (" ")



while True:
    print("P",puls)
    xbmcgui.Window(10000).setProperty('Pulsy', puls)
    time.sleep(1)
    print("P",zero)
    xbmcgui.Window(10000).setProperty('Pulsy', zero)
    time.sleep(1)