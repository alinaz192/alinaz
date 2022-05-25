from tkinter import * # imports everything from TK

root= Tk() # top level window
def callback():
    label.config(text='You clciked me', fg='red', bg='yellow')
#Here is have added font colour and background
#colour on click

#Cretae label
label= Label(root, text="Hello Phyton")
label.pack()

#Create button (now with the command function)
button= Button(root, text="Click Me!", command =callback)
button['state']='disabled' #can disable thr button
button['state']='normal' #back to normal
button.pack()

root.geometry("350x300")
root.mainloop()

