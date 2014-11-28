#! /usr/bin/env python
# coding:utf-8
from lib.request_util import *
import time

def generate_data(boundary,filename):
	data = []
        data.append('--%s' % boundary)
        
        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'username')
        data.append('jack')
        data.append('--%s' % boundary)
        
        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'mobile')
        data.append('13800138000')
        data.append('--%s' % boundary)
        
#       fr=open(r'/var/qr/b.png','rb')
        data.append('Content-Disposition: form-data; name="profile"; filename="%s"' % filename)
        data.append('Content-Type: %s\r\n' % 'image/png')
#       data.append(fr.read())
#       fr.close()
        data.append('--%s--\r\n' % boundary)

	return data
	

def check_upload_usecase(info,domain,method,i):
	print "----------------"
#	print i,":",info
	boundary = '----------%s' % hex(int(time.time() * 1000))
	data = generate_data(boundary,info)
	upload_data = '\r\n'.join(data)
#	print upload_data
	req_headers = {"Content-Type": "multipart/form-data; boundary=%s" % boundary,
			"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"}
	res = check_usecase("/search.php",method,upload_data,req_headers,domain)
	
	if res == 200:
		print '\033[1;31;40m'
		print i,":",res,"   usecase:",info
		print '\033[0m'
	else:
		print i,":",res,"   usecase:",info	

def UPLOAD_TEST(domain,method,usecase):
	upload_file = open(usecase)
	file_content_lines = upload_file.readlines()
	upload_file.close()
	i = 0
	for line in file_content_lines:
		info = line.strip()
		i+=1
		if info != "":
			check_upload_usecase(info,domain,method,i)
			time.sleep(5)
