#__*__ coding: CP949 __

import os
import sys
import urllib.request

access_key = 'BYh2HVZz6zs8ZhXVXeHD6jj8GEMaX6VfrShv4yUC3dtT5BhHLS7us4DGGWPJ%2BhA%2FUX%2FgBrF2o87ePN5BVX5S8g%3D%3D'

def get_request_url(url):
    
    req = urllib.request.Request(url)
    
    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


if __name__ == "__main__":
    end_point = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"
    
    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&YM=" + yyyymm
    parameters += "&SIDO=" + urllib.parse.quote(sido)
    parameters += "&GUNGU=" + urllib.parse.quote(gungu)
    parameters += "&RES_NM=&pageNo=" + str(nPagenum)
    parameters += "&numOfRows=" + str(nItems)

    url = end_point + parameters

    print("*******")
    print("URL==> " + url)

    get_request_url(url)

