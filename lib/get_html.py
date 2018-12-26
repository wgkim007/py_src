# __*__ coding: CP949 __*__

import  sys
import  requests

HTML_F = "html.txt"

def getHtml(url):

    res = requests.get(url)
    text = res.content.decode('UTF-8') #한글 깨지지 않음

    return text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\t Usage: %s [url]" % sys.argv[0])
        exit 
    else:
        URL = sys.argv[1]
        ret = getHtml(URL)
        print(ret)

        with open(HTML_F, "w") as fd:
            fd.write(ret)
