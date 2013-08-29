#coding:utf-8
import os
import sys,os,datetime
from croniter import *
import time


class Plugin:
    def setPlatform(self, platform):
        self.platform=platform

    def start(self):
    	schedule = self.schedule()
    	now = datetime.datetime.now()
        itr = croniter(schedule,now)
        next = itr.get_next(datetime.datetime)
        while(True):
			if(datetime.datetime.now()>next):
				next = itr.get_next(datetime.datetime)
				self.run()
			time.sleep(1)

    def stop(self):
        self.platform.sayGoodbye("plugin")
        
    def run(self):
	   pass
	  
    def schedule(self):
        pass

def getPluginClass():
    return Plugin


