# _*_ coding: UTF-8 _*_

import sys
from lib.getSoup_mdl import *

URL = "https://www.kotra.or.kr/kh/about/KHKINY150M.do?MENU_CD=&TOP_MENU_CD=G0100&LEFT_MENU_CD=G0101&PARENT_MENU_CD=&YEAR_MONTH=&nation=1301"

def File_Sample(HTML_F):
	with open(HTML_F, 'r', encoding='UTF-8') as fd:
		lines = fd.readlines()
	for html in lines:
		soup = get_soup(html)
		print("File_Read=%s" % soup)

		tag = find_attr(soup, 'td', 'title')
		print("File_Read=%s" % tag)

	return

def URL_Sample(url, key):
	soup = get_url_soup(url)

#       nation = soup.find_all(key)
#	print("Search = %s " % nation)

	tags = find_all_attr(soup, "tr", "option")
	print("FindALL = %s " % tags)

	count = 0
	for tag in tags:
		count = count + 1
		print("TAG=[%s] " % (tag.a.text))
		

if __name__ == "__main__":

	if len(sys.argv) != 3 : 
		print("\t Usage : %s [URL : FILE] [url_site : file_name]" % sys.argv[0])
	else : 
		if sys.argv[1] == "URL" : 
			URL_Sample(URL, sys.argv[2])
		elif sys.argv[1] == "FILE" : 
			FileName = sys.argv[2]
			File_Sample(FileName, sys.argv[2])
		else : 
		        print("\t Usage : %s [URL : FILE] [url_site : file_name]" % sys.argv[0])

