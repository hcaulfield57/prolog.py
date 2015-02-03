import datetime
import prolog
import sys
import util
import window

def main():
    # defaults
    gui   = True
    today = datetime.date.today() - datetime.timedelta(13)

    # parse command line arguments
    if len(sys.argv) > 3:
        util.usage()
    for i in sys.argv[1:]:
        if i == '-d':
            gui = False
        elif '/' in i:
            today = util.parsedate(i)
        else:
            util.usage()

    # setup internal representation of the date
    plg = prolog.Prolog(today)

    # determine whether we are running the gui or not
    if gui:
        win = window.Window(plg)
    else:
        sys.stdout.write('{0}\n'.format(str(plg)))
        sys.exit()

# main entrypoint
main()
