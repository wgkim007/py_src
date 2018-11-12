#__coding__: UTF-8
#한글지원방법: euc_kr-완성형, utf-8, 16 - 조합형

# 다른 파일의 함수를 Call 해서 사용할때 
import sys
LIB_PATH="/home/Administrator/wgkim/py_src/lib"
sys.path.append(LIB_PATH)

from file_sub import *

name_list = ["Kim Weon Geol1\n", "Jeong Hye Jun2\n", "Kim Seong Hyun3\n", "Kim Seong Yun4\n"]

# 항상 습관적으로 사용: 함수 call 할때 불필요한 출력 방지
if __name__ == "__main__":
    
    fp = file_open("aa.txt", "a")
    for name in name_list:
        file_write(fp, name)
    file_close(fp)

    fp = file_open("aa.txt", "r")
    while True:
        line = file_read(fp)
        if not line: break
        print("*** READ_LINE=%s"%line)

    file_close(fp)

    fp = file_open("aa.txt", "r")
    lines = file_reads(fp)
    for line in lines:
        print(">>> Read_LINES="+line)
    
    file_close(fp)
