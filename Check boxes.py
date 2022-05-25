 # This program shows Grid Manager - which helps us to organise our widgets easily
from tkinter import *
from tkinter import ttk
root = Tk()

def callback():
    val1 = entry.get()
    val2 = entry2.get()
    print("Your name is:" + val1)
    print("Your Password is :" +val2)

# create entries
entry = ttk.Entry(root, width=30)
entry2 = ttk. Entry(root, width=30)
# create placeholder
entry.insert(0,'Please enter your name')
entry2.insert (0, 'Please enter your password' )
# create button and labels
button = ttk.Button(root, text='Enter' )
lbltitle = ttk.Label(text='Our Title Here', font=(('Arial'), 22))
lblname = ttk.Label(text='Your Name : ')
lblpass = ttk.Label(text='Your Password: ')
# position of the buttons, labels and entries as outcome
lbltitle.grid(row=0, column=0)
lblname.grid(row=1, column=0)
lblpass.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1)


#button.grid(row=3, column=2, sticky= E+W)#E+W spans it across the vell in that coloumn
#button.grid(row=3, column=1, sticky= E) #will have the button on the right
#button.grid(row=3, column=1, sticky= W) will put button on the left side
#gives you a bit og a gap between the two rows
button.grid(row=3, column=1, sticky=E, pady=5)

# checkbox
chvar = IntVar() #checkbox variable
chvar.set(0) #set to 0 (zero) - means not checked

# checkbox variable
cbox = Checkbutton (root, text='Remember Me', variable=chvar,
                    font='Arial 16'). grid(row=4, column=0)
# sticky=E, coloumnspan=2 # in order to get it align right 

root.geometry('500x450')
root.mainloop()
