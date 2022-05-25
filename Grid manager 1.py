 # This program shows Grid Manager - which helps us to organise our widgets easily
from tkinter import *
from tkinter import ttk
root = Tk()

def callback(): #callback function
    print("Your Name:"+_entry.get())
    print("Your Password :"+entry2.get())
    if chvar.get ()==1:  #means the checkbox is checked
        print("Remember me selected")
    else:
        print("notslected")
        print(gender.get())    # this is were to get our gender value to show when we run the program
        #this is were to get our gender value to show when we run the program
        print(gender.get())
        

root= Tk()


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

#checkbox
chvar= IntVar() # checkbox variable
chvar.set(0) # set to 0 (zero) - means not checked

# checkbox variable
cbox = Checkbutton(root, text='Remember Me', variable=chvar,
                   font='Arial 16').grid(row=4, column=0)
# sticky =E, columnspan=2 # in order to get it align right


#button.grid(row=3, column=2, sticky= E+W)#E+W spans it across the vell in that coloumn
#button.grid(row=3, column=1, sticky= E) #will have the button on the right
#button.grid(row=3, column=1, sticky= W) will put button on the left side
#ggives you a bit og a gap between the two rows
button.grid(row=3, column=1, sticky=E, pady=5)

#create radio button
#to get the value from our radio button - in the callback function
ttk.Radiobutton(root, text='Female', value='Female', var=gender).grid(row=5, column=0)
ttk.Radiobutton(root, text='Male', value='Male', var=gender).grid(row=5, column=1)



root.geometry('500x450')
root.mainloop()
