#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Instagram username availablity checker.
# Coded by @4201337
# https://github.com/4201337
# ---------------------

from multiprocessing.dummy import Pool as ThreadPool
from threading import Lock as LockPool
import requests
import time
import sys

myList = open('list.txt').readlines()
myThreads = 25
myLock = LockPool()
myPool = ThreadPool(myThreads)

def myRun(username):
	username = username.strip()
	url = 'https://www.instagram.com/'
	req = requests.get(url + username)
	if req.status_code == 200:
		with myLock:
			print("NotVoided") , username
		with open('NotVoided.txt', 'a') as NotVoided:
			NotVoided.write(username + '\n')
	elif req.status_code == 404:
		with myLock:
			print("Voided") , username
		with open('Voided.txt', 'a') as Voided:
			Voided.write(username + '\n')
	else:
		with myLock:
			print("Error") , username
		with open('Error.txt', 'a') as Error:
			Error.write(username + '|' + req.status_code + '\n')

startTime = time.time()

if __name__ == '__main__':
    myPool.map(myRun, myList)
    myPool.close()
    myPool.join()

endTime = time.time()

print("===============================")
print("Done!")
print("===============================")
print("Total Time    :") , round(endTime - startTime, 2) , 'Seconds'
print("Total Threads :")  , myThreads
print("Total Tries   :")  , len(myList)
print("===============================")
print("Thank you for using Void Check!")
print("Void Checker By @KingLiammmm!")
print("===============================")