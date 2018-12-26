# __*__ coding: EUC-KR __*__

def euc_2_utf8(euc):
    utf = unicode(euc, 'utf-8').encode('euc-kr')
    return utf


if __name__ == "__main__":
    euc = "rocksea 블로그"
    print("EUC = %s" % euc)

    utf = euc_2_utf8(euc)
    print("EUC = %s" % utf)
