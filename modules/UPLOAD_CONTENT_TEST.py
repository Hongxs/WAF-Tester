#! /usr/bin/env python
# coding:utf-8
from lib.request_util import *
import time,os,sys

i = 0
def generate_data(boundary,filepath):
	data = []
        data.append('--%s' % boundary)
        
        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'username')
        data.append('jack')
        data.append('--%s' % boundary)
        
        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'mobile')
        data.append('13800138000')
        data.append('--%s' % boundary)

	try:        
        	fr=open(filepath,'rb')
	except Exception ,e:
		print e
       	data.append('Content-Disposition: form-data; name="profile"; filename="%s"' % 'test.jpg')
        data.append('Content-Type: %s\r\n' % 'image/jpeg')
	data.append('testtesttest!')
        data.append(fr.read())
        fr.close()
        data.append('--%s--\r\n' % boundary)

	return data
	

def check_upload_usecase(filepath,domain,method,i):
	print "----------------"
#	print i,":",info
	boundary = '----------%s' % hex(int(time.time() * 1000))
	data = generate_data(boundary,filepath)
	upload_data = '\r\n'.join(data)
	#print upload_data
	req_headers = {"Content-Type": "multipart/form-data; boundary=%s" % boundary,
			"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"}
	res = check_usecase("/search.php",method,upload_data,req_headers,domain)
	
	if res == 403:
                print i,":",res,"   usecase:",filepath
        else:
                print '\033[1;31;40m'
                print i,":",res,"   usecase:",filepath
                print '\033[0m'	

def UPLOAD_CONTENT_TEST(domain,method,usecase):
#	upload_file = open(usecase)
#	file_content_lines = upload_file.readlines()
#	upload_file.close()
	global i
	oldpath = usecase
	filelist = os.listdir(oldpath)
	for name in filelist:
		newpath = os.path.join(oldpath,name)
		if os.path.isdir(newpath):
			usecase = newpath
			UPLOAD_CONTENT_TEST(domain,method,usecase)
			usecase = oldpath
		else:
			i = i + 1
			check_upload_usecase(newpath,domain,method,i)
			time.sleep(5)
