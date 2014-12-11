#! /usr/bin/env python
# coding:utf-8
from lib.request_util import *
import time

def check_sqli_usecase(info,domain,method,i):
	print "----------------"
#	print i,":",info
	res = check_usecase("/search.php",method,{"keyword":info},None,domain)
	
	if res == 403:
                print i,":",res,"   usecase:",info
        else:
                print '\033[1;31;40m'
                print i,":",res,"   usecase:",info
                print '\033[0m'

def SQLI_TEST(domain,method,usecase):
	sqli_file = open(usecase)
	file_content_lines = sqli_file.readlines()
	sqli_file.close()
	i = 0
	method = method
	for line in file_content_lines:
		info = line.strip()
		i+=1
		if info != "":
			check_sqli_usecase(info,domain,method,i)
			time.sleep(5)
