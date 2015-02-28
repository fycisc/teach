# -*- coding: utf-8 -*-
__author__ = 'feiyicheng'
from variables import *
from testmedia import *
from os import system
import time

def getcurrentnum(content, maxnum):
	tag = -1
	num = maxnum
	while tag==-1:
		tag = content.find( '<td class="bg5" align="center" width="10%">' + str(num) + '</td>')
		num -= 1
	return num+1

def notifyMe():
	playNotify()

def celebrateMe():
	playCelebrate()

def insertMe(url, logfile):
	content = opener.open(url).read()
	logfile.write('url: ' + url + ' || content: ' + content + '\n')
	if content.startswith('D'):
		return 0 # success
	else:
		return -1 # fail


def scan():
	logfile = open("./teach.log","a")
	for classentry in classes:
		(url,maxnum,classname, inserturl, sid) = classentry
		content = opener.open(url).read()
		currentnum = getcurrentnum(content, maxnum)
		if currentnum<maxnum:
			# tell me which class is availble
			cmd = 'say '+ classname
			system(command=cmd)

			# write log
			logfile.write( '-------------' + time.strftime( '%Y-%m-%d-%H:%M:%S',
															time.localtime( time.time( ) ) ) + '-----------\n' )
			logfile.write(
				classname + 'current: ' + str( currentnum ) + ' max: ' + str( maxnum ) + '\n' )  # insert me into that class
			for i in xrange(10):
				if insertMe(url=inserturl, logfile=logfile)==0: # success
					celebrateMe()
					break
				else: # fail
					notifyMe()
	logfile.close()


if __name__ == '__main__':
	loopnum = 0
	while True:
		scan()
		loopnum += 1
		print("scanning #" + str(loopnum))
		time.sleep(deltatime)
