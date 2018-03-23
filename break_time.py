#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 21:56:16 2018

@author: dewayneroy
"""

import time
import webbrowser 

total_breaks = 3
break_count = 0 

print("This program started on " +time.ctime())
while (break_count < total_breaks):
    time.sleep(7200) 
    webbrowser.open("https://www.youtube.com/watch?v=Eegftbcv9Ug") 
    break_count = break_count + 1
