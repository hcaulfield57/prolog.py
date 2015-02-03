import datetime
import sys

def parsedate(date):
    if len(date) != 5:
        usage()

    month = date[0:2]
    day   = date[3:5]
    today = datetime.date.today() # throw away

    return datetime.date(today.year, int(month), int(day))

def usage():
    sys.stderr.write('usage: prolog [-d] [MM/DD]\n')
    sys.exit(1)
