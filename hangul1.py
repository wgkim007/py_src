# __*__ coding: CP949 __*__

import requests

url = 'http://finance.naver.com/' #euc-kr (CP949)

res = requests.get(url)
text = res.content.decode('euc-kr') #�ѱ� ������ ����

print(text)

