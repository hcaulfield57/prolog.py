import Tkinter as Tk

class Window(object):
    def __init__(self, plg):
        self.plg  = plg
        self.root = Tk.Tk()

        self.root.title('Prolog from Ochrid - ' + self.plg.title())

        # buttons
        self.yesterdaybtn = Tk.Button(self.root, text='Yesterday')
        self.yesterdaybtn.grid(row=0, column=0)

        self.todaybtn = Tk.Button(self.root, text='Today')
        self.todaybtn.grid(row=0, column=1)

        self.tomorrowbtn = Tk.Button(self.root, text='Tomorrow')
        self.tomorrowbtn.grid(row=0, column=2)

        # display
        self.displaytext = Tk.Text(self.root)
        self.displaytext.grid(row=1, column=0, columnspan=3)
        self.displaytext.insert(Tk.INSERT, str(self.plg))
        self.displaytext.config(state=Tk.DISABLED)

        self.root.mainloop()
