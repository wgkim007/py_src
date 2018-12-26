#__coding: UTF-8__

import	os
import	sys
import 	urllib.request

from bs4 import BeautifulSoup

# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def get_soup(a_html):
	soup = BeautifulSoup(a_html, 'html.parser')
	return soup

def get_url_soup(url):
	html = urllib.request.urlopen(url)
	soup = BeautifulSoup(html, 'html.parser')
	return soup

def find_attr(soup, arg1, arg2):
	tag = soup.find(arg1, attrs={'class':arg2})
	return tag

def find_all_attr(soup, arg1, arg2):
	tag = soup.findAll(arg1, attrs={'class':arg2})
	return tag
