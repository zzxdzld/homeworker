from tkinter import *
class Print:
	def __init__(self,text,title):
		x=Tk()
		info=messagebox.showinfo(title=title,message=text,\
                                         option=default)
