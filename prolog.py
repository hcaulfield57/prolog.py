import datetime

class Prolog(object):
    def __init__(self, today):
        self.today = today

    # in place modification of current date
    def next(self):
        self.today = self.today + datetime.timedelta(1)

    def prev(self):
        self.today = self.today - datetime.timedelta(1)

    # path representation for file manipulation
    def path(self):
        return 'files/{0}/{1}.html'.format(self.today.month, self.today.day)

    # used to obtain actual information
    def __str__(self):
        return self.read()

    # attempt to read the correct date from the file tree
    # Note: in the event that the files are missing from the current
    # directory, this method will fail.
    def read(self):
        dayfile = open(self.path(), 'rb')
        lines   = dayfile.readlines()
        text    = ''
        for i in lines:
            text = text + i
        return text
