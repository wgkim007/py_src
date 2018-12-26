#__coding: UTF-8__

import sys
from lib.getSoup_mdl import *

def File_Sample(HTML_F):
	with open(HTML_F, 'r', encoding='UTF-8') as fd:
		lines = fd.readlines()
	for html in lines:
		soup = get_soup(html)
		print("File_Read=%s" % soup)

		tag = find_attr(soup, 'td', 'title')
		print("File_Read=%s" % tag)

	return

def URL_Sample(url):
	soup = get_url_soup(url)
	tags = find_all_attr(soup, "div", "tit3")
#	print("FindALL = %s " % tags)

	count = 0
	for tag in tags:
		count = count + 1
		print("영화 순서 : (%02d 위) [%s] " % (count, tag.a.text))
		

if __name__ == "__main__":

	if len(sys.argv) != 3 : 
		print("\t Usage : %s [url : file] [URL : FileName]" % sys.argv[0])
	else : 
		if sys.argv[1] == "url" : 
			URL = sys.argv[2]
			URL_Sample(URL)
		elif sys.argv[1] == "file" : 
			FileName = sys.argv[2]
			File_Sample(FileName)
		else : 
			print("\t Usage : %s [url : file] [URL : FileName]" % sys.argv[0])

