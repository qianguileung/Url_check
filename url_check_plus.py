# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests
import time
from multiprocessing.dummy import Pool as ThreadPool
import re
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def main():
	dic=[]
	try:
		with open("url.txt") as f:
				for line in f:
					url="http://"+line.strip()
					dic.append(url)
		pool = ThreadPool(100)	
		pool.map(geturl, dic)
	except:
		print "ERROR"
def geturl(url):
	try:
		r=requests.get(url,timeout=1.3);
		print '\033[0m[*]\t'+url+"\n"
		if (r.status_code ==200):
			if(re.findall(r'password',r.text,re.M)):
				print '\033[5;32m[+]\t'+url+"\n"
				with open('out.txt') as file:
					if url not in file.read():
						f2 = open('out.txt','a+')
						f2.write(url+"\n")
						f2.close()
	except:
		print '\033[1;31m[!]\t'+url+'\n'
main()	
									