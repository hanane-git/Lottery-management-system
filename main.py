from tkinter import *
from pl import main_form
screen=Tk()
screen.config(bg="#FFB5A7")
screen.geometry("700x600")
screen.title("Lottery Form")
screen.resizable(False,False)
main_form.MyApp(screen)
screen.mainloop()

