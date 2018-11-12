#__coding__: UTF-8

def file_open(filename, opt):
    fp = open(filename, opt)
    return fp

def file_read(fp):
    line = fp.readline()
    return line

def file_reads(fp):
    lines = fp.readlines()
    return lines

def file_write(fp, data):
    fp.write(data)

def file_close(fp):
    fp.close()
