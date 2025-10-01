from tkinter import Tk
from ui.diario import RegistroManual

if __name__ == '__main__':
    #print('Probando')
    root = Tk()
    app = RegistroManual(root)
    root.mainloop()