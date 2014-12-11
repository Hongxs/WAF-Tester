WAF-Tester

========


WAF 测试工具 --- 用例测试


直接运行./exploit.py，运行结果返回403为被WAF拦截，否则为漏报！

#=====================================

#-t type : test type (eg:sqli,xss,commandi,lfi,upload_ext,upload_content,download,spider)

#-m method: test method (eg:get,post)

#-d domain : test domain (eg:http://www.xxx.com/)

#-u usecase : test usecase 

#Usage:
	
./exploit.py -t <type> -m <method> -d <domain> [-u <usecase>]
	
./exploit.py -t sqli -m get -d http://www.xxoo.com -u usecase/sqli.usecase

#=====================================


如果没有指定 -u [用例路径]，就采用默认的用例。如自己指定需要测试的用例，就会采用指定的用例。



类型说明：
sqli		检测SQL注入			
xss		检测跨站脚本攻击		
commandi	检测命令注入攻击
lfi		检测本地文件包含/目录遍历攻击
download	检测非法文件下载
spider		检测恶意爬虫
upload_ext	检测上传文件的后缀名
upload_content	检测上传文件的内容	---默认用例：usecase/upload_content，其中用例以文件为单位，放入文件夹可以递归


每发个请求，睡眠5秒！
由于用例是经验整理的，可能有的欠妥！