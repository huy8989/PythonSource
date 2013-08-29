#coding:utf-8
import os
import sys,os,datetime
from croniter import croniter
from plugin import *
import winsound

class AlertPlugin(Plugin):
    def run(self):
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

    def schedule(self):
        return '*/1 * * * * *'
def getPluginClass():
    return AlertPlugin


