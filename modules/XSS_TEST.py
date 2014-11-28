#! /usr/bin/env python
# coding:utf-8
from lib.request_util import *
import time

def check_xss_usecase(info,domain,method,i):
        print "----------------"
#       print i,":",info
        res = check_usecase("/search.php",method,{"keyword":info},None,domain)
#        print i,":",res,"   usecase:",info
	if res == 200:
                print '\033[1;31;40m'
                print i,":",res,"   usecase:",info
                print '\033[0m'
        else:
                print i,":",res,"   usecase:",info

def XSS_TEST(domain,method,usecase):
        xss_file = open(usecase)
        file_content_lines = xss_file.readlines()
        xss_file.close()
        i = 0
        for line in file_content_lines:
                info = line.strip()
                i+=1
                if info != "":
                        check_xss_usecase(info,domain,method,i)
			time.sleep(5)
