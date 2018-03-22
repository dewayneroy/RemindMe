#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 21:56:16 2018

@author: dewayneroy
"""

import time #Step3
import webbrowser #Step1

total_breaks = 3 #Step5
break_count = 0 #Step6

print("This program started on " +time.ctime())
while (break_count < total_breaks): #Step7
    time.sleep(2700) #Step 4
    webbrowser.open("https://www.youtube.com/watch?v=Eegftbcv9Ug") #Step2
    break_count = break_count + 1
