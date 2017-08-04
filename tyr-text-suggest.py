# -*- coding: utf-8 -*-
import textSuggestClass as tsc

pd = "Pythonを使ってみたい。"

test = tsc.textSuggestClass()
for i in range(10):
    pd = test.outText(pd,0,2)
print (pd)