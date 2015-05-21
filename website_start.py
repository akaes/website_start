#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import webbrowser
import threading

url = 'https://www.' #insert url
def hello():
    webbrowser.open_new_tab(url)

t = threading.Timer(0.0, hello) #insert seconds
t.start()
