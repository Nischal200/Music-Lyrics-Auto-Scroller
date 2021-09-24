# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import threading
import pyautogui
from pynput.keyboard import Listener

speed = input("Scrooll Speed")
sleepTime = input("Scroll Spacing")

pyautogui.time.sleep(3)

def on_press(key):
    if key.char == 'e':
        print("here")
        sys.exit("test")


def on_release(key):
    if key.char == 'e':
        quit()


def listen():
    while 0 < 10:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()


thread = threading.Thread(target=listen)
thread.start()

while 0 < 10:
    pyautogui.scroll(int(speed))
    pyautogui.time.sleep(int(sleepTime))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
