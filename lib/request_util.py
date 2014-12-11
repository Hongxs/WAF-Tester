#! /usr/bin/env python 
# coding:utf-8

import urllib,urllib2,socket
import random,types
socket.setdefaulttimeout(10)

def send_req_get(url,params=None,headers=None):
        if params:
                params_str = urllib.urlencode(params)
                url = "%s?%s" % (url,params_str)
                req = urllib2.Request(url,headers=headers)
        else:
                req = urllib2.Request(url,headers=headers)
        try:
                response = urllib2.urlopen(req)
                res = response.getcode()
        except urllib2.HTTPError,e:
                res = e.code
				pass
				
        return res

def send_req_post(url,params=None,headers=None):
	if params:
		if type(params) is types.DictType:
			params = urllib.urlencode(params)
		req = urllib2.Request(url,data=params,headers=headers)
	else:
		req = urllib2.Request(url,headers=headers)
	try:
		f = urllib2.urlopen(req)
		res = f.getcode()
	except urllib2.HTTPError,e:
		res = e.code
		pass
		
	return res

def randomIP():
	clientip = ""
	for i in range(3):
		temp = random.randint(0,255)
		clientip += str(temp) + "."
	clientip = clientip + str(random.randint(0,255))
	return clientip

def check_usecase(uri,method,params,req_headers,host):
	url = host + uri
	clientip = randomIP()
	if req_headers == None:
		req_headers={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6",
			"X-Forwarded-For": clientip}
	else:
		req_headers['X-Forward-For'] = clientip
#	print clientip
	if method == "get":
		res = send_req_get(url,params,req_headers)
	elif method == "post":
		res = send_req_post(url,params,req_headers)
	else:
		res = 503
	return res
