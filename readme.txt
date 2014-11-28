WAF-Test

========


WAF 测试工具 --- 用例测试


直接运行./exploit.py，运行结果返回403是被WAF拦截，返回200就是漏报！

#=====================================

#-t type : test type (eg:sqli,xss,commandi,lfi,upload,download,spider)

#-m method: test method (eg:get,post)

#-d domain : test domain (eg:http://www.xxx.com/)

#-u usecase : test usecase 

#Usage:
	
./exploit.py -t <type> -m <method> -d <domain> [-u <usecase>]
	
./exploit.py -t sqli -m get -d http://www.xxoo.com -u usecase/sqli.usecase

#=====================================


如果没有指定 -u [用例路径]，就采用默认的用例。如自己指定需要测试的用例，就会采用指定的用例。



由于用例是经验整理的，可能有的欠妥！