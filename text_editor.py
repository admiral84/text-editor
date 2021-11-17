from tkinter import *  
#creating the application main window.   
top = Tk()
#get the screen size
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()
#Entering the event main loop
#the frame geometrie
top.geometry(f"{screen_width}x{screen_height}")
menubutton = Menubutton(top, text = "file", relief = FLAT)
menubutton.grid()  
  
menubutton.menu = Menu(menubutton)
menubutton["menu"]=menubutton.menu  

top.mainloop()  