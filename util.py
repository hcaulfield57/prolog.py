import datetime
import sys

def parsedate(date):
    if len(date) != 5:
        usage()

    month = date[0:2]
    day   = date[3:4]
    return month, day

def usage():
    sys.stderr.write('usage: prolog [-d] [MM/DD]\n')
    sys.exit(1)
