# _*_ coding : CP949 _*_

import sys
from lib.getSoup_mdl import *

URL = "https://www.kotra.or.kr/kh/about/KHKINY150M.do?MENU_CD=&TOP_MENU_CD=G0100&LEFT_MENU_CD=G0101&PARENT_MENU_CD=&YEAR_MONTH=&nation=1301"

def Soup_Find(tag):
    soup = get_url_soup(URL)

#    title_data = soup.find(tag)
#    print(title_data)
#    print(title_data.string)
#    print(title_data.get_text())

    all_country = find_all(soup, tag)

    for country in all_country:
        if country.string == "중국" : 
            print(country)


#	    tag = soup.find(tag, attrs={'value':arg2})
#	    tag = soup.findAll(arg1, attrs={'class':arg2})

            rval = soup.find('value')
            print("Nation Code = %s" % rval.get_text())
 
# Main
if __name__ == "__main__" : 
    tag = sys.argv[1]
    Soup_Find(tag)
 
