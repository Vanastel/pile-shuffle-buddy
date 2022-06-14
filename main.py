#!/usr/bin/env python3

import pyautogui as py #Import pyautogui
import time #Import Time
import cv2 as cv 
import os

icons = os.listdir(r"../Pile/icons")
prefix = "../Pile/icons/"
iconPathList = []
for i in icons:
    iconPathList.append(prefix + i)

## Start WoW ##
def Start_WOW():
    start, bnet = py.locateCenterOnScreen(iconPathList[iconPathList.index(prefix + 'bnet.png')], confidence=0.9)
    py.moveTo(start, bnet)
    py.click()
    time.sleep(5)
    play, but = py.locateCenterOnScreen(iconPathList[iconPathList.index(prefix + 'play.png')], confidence=0.9)
    py.moveTo(play, but)
    py.click()
    time.sleep(20)
    tailor, shuffle = py.locateCenterOnScreen(iconPathList[iconPathList.index(prefix + 'tinyspell.png')], confidence=0.9)
    py.moveTo(tailor, shuffle)
    py.doubleClick()
    time.sleep(10)

## Start Tailor shuffle ##
def Start_tailor():
    py.hotkey("k")
    time.sleep(3)
    tailoring, icon = py.locateCenterOnScreen(iconPathList[iconPathList.index(prefix + 'tailoring.png')], confidence=0.9)
    py.moveTo(tailoring, icon, .5)
    py.click()

## Open Vendor ##
def Open_vendor():
    py.hotkey("1") # Macro in game to target vendor
    time.sleep(.25)
    py.hotkey(".") # Interact with NPC keybind
    time.sleep(1)
    sell, tsm = py.locateCenterOnScreen(iconPathList[iconPathList.index(prefix + 'sell_tsm.png')], confidence=0.9)
    time.sleep(1)
    py.click(sell, tsm)

## Shrouded Cloth Robe Profile ##
def Shrouded_Robe_Profile():
    search, patterns = py.locateCenterOnScreen(iconPathList[iconPathList.index(prefix + 'search_patterns.png')], confidence=0.9)
    py.moveTo(search, patterns, .25)
    py.click()
    py.write("Shrouded Cloth Robe")

Start_WOW()
Start_tailor()
Open_vendor()
Shrouded_Robe_Profile()

for i in range(0,99):
    craft, all = py.locateCenterOnScreen(iconPathList[iconPathList.index(prefix + 'craft_all.png')], confidence=0.9)
    py.moveTo(craft, all, 1)
    py.doubleClick()
    time.sleep(285)
    for n in range(0, 14):
        sell, boe = py.locateCenterOnScreen(iconPathList[iconPathList.index(prefix + 'sell_boe.png')], confidence=0.9)
        py.moveTo(sell, boe, 1)
        py.click()
        time.sleep(1.5)

    




## Shufflebuddy v.2 ##

# img = cv.imread(r"c:/Projects/Pile/") 

# ## Start WoW ##
# def Start_WOW():
#     start, bnet = py.locateCenterOnScreen("bnet.png", confidence=0.9)
#     py.moveTo(start, bnet)
#     py.click()
#     time.sleep(5)
#     play, but = py.locateCenterOnScreen("play.png", confidence=0.9)
#     py.moveTo(play, but)
#     py.click()
#     time.sleep(20)
#     tailor, shuffle = py.locateCenterOnScreen("tinyspell.png", confidence=0.9)
#     py.moveTo(tailor, shuffle)
#     py.doubleClick()
#     time.sleep(10)

# ## Start Tailor shuffle ##
# def Start_tailor():
#     py.hotkey("k")
#     time.sleep(3)
#     tailoring, icon = py.locateCenterOnScreen("tailoring.png", confidence=0.9)
#     py.moveTo(tailoring, icon, .5)
#     py.click()

# ## Open Vendor ##
# def Open_vendor():
#     py.hotkey("1")
#     time.sleep(.25)
#     py.hotkey(".")
#     time.sleep(1)
#     sell, tsm = py.locateCenterOnScreen("sell_tsm.png", confidence=0.9)
#     time.sleep(1)
#     py.click(sell, tsm)

# ## Shrouded Cloth Robe Profile ##
# def Shrouded_Robe_Profile():
#     search, patterns = py.locateCenterOnScreen("search_patterns.png", confidence=0.9)
#     py.moveTo(search, patterns, .25)
#     py.click()
#     py.write("Shrouded Cloth Robe")

# Start_WOW()
# Start_tailor()
# Open_vendor()
# Shrouded_Robe_Profile()

# for i in range(0,99):
#     craft, all = py.locateCenterOnScreen("craft_all.png", confidence=0.9)
#     py.moveTo(craft, all, 1)
#     py.doubleClick()
#     time.sleep(285)
#     for n in range(0, 14):
#         sell, boe = py.locateCenterOnScreen("sell_boe.png", confidence=0.9)
#         py.moveTo(sell, boe, 1)
#         py.click()
#         time.sleep(1.5)



##Shufflebuddy##
## Point and Click v.1 ##
# for i in range(0, 36):
#     py.moveTo(98,577, 1)
#     py.click(98,577, 2)
#     time.sleep(285)
#     for n in range(0, 14):
#         py.moveTo(1050,493, 1)
#         py.click(1050,493, 2)
#         time.sleep(1.5)
# if i == 36:
    # py.press('esc', presses=3)
    # py.moveTo(967,630)
    # py.click(967,630, 2)

## Mouse Position Printer ##
# while True: #Start loop
#    print (py.position())
#    time.sleep(1)

