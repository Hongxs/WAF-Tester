WAF-Test

========


WAF ���Թ��� --- ��������


ֱ������./exploit.py�����н������403Ϊ��WAF���أ�����Ϊ©����

#=====================================

#-t type : test type (eg:sqli,xss,commandi,lfi,upload_ext,upload_content,download,spider)

#-m method: test method (eg:get,post)

#-d domain : test domain (eg:http://www.xxx.com/)

#-u usecase : test usecase 

#Usage:
	
./exploit.py -t <type> -m <method> -d <domain> [-u <usecase>]
	
./exploit.py -t sqli -m get -d http://www.xxoo.com -u usecase/sqli.usecase

#=====================================


���û��ָ�� -u [����·��]���Ͳ���Ĭ�ϵ����������Լ�ָ����Ҫ���Ե��������ͻ����ָ����������



����˵����
sqli		���SQLע��			
xss		����վ�ű�����		
commandi	�������ע�빥��
lfi		��Ȿ���ļ�����/Ŀ¼��������
download	���Ƿ��ļ�����
spider		����������
upload_ext	����ϴ��ļ��ĺ�׺��
upload_content	����ϴ��ļ�������	---Ĭ��������usecase/upload_content�������������ļ�Ϊ��λ�������ļ��п��Եݹ�




���������Ǿ�������ģ������е�Ƿ�ף�