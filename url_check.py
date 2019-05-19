# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests
import time
import threading
import re
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def main():
	for i in range(1):
		add_thread = threading.Thread(target=geturl)
		add_thread.start()
		add_thread.join()
def geturl():
	try:
		with open("url.txt") as f:
				for line in f:
					url="http://"+line.strip()
					try:
						r=requests.get(url,timeout=1.3);
						print '\033[1;33m'+url+"   code:",
						print(r.status_code) 
						if (r.status_code ==200):
							if(re.findall(r'password',r.text,re.M)):
								print '\033[5;32m'+url + '     ======>OK'
								with open('out.txt') as file:
									if url not in file.read():
										f2 = open('out.txt','a+')
				                        f2.write(url+"\n")
				                        f2.close()
					except:
						print '\033[1;31mERROR'+"   "+url   
						continue
	except:
		print "ERROR"
#过滤无用的信息
def Clear():
	url=[]
	with open("url.txt") as f:
			for line in f:
					if "127.0.0.1" not in line:
						print line,
						with open('out.txt') as file:
									if url not in file.read():
										f2 = open('out.txt','a+')
				                        f2.write(url+"\n")
				                        f2.close()
main()			
									