import datetime
import sys

def getdate():
    today = datetime.date.today()
    jdate = today - datetime.timedelta(13)
    return jdate.month, jdate.day

def isdefined(var):
    if var is not None:
        return True
    else:
        return False

def parsedate(date):
    if len(date) != 5:
        usage()

    month = date[0:2]
    day   = date[3:4]
    return month, day

def usage():
    sys.stderr.write('usage: prolog [-d] [MM/DD]\n')
    sys.exit(1)
