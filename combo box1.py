from tkinter import *
from tkinter import ttk


root = Tk()

# When enter is pressed
def callback():
    val1 = entry.get()
    val2 = entry2.get()

    print("Your Name is: " + val1)
    print("Your Password is: " + val2)
    if chvar.get() == 1:
        print("O_O")
    else:
        print("oh ok...")
    print(gender.get())

# create entries
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

#placeholder
entry2.config(show='*')

#button and label creation
button = ttk.Button(root, text='Enterrr', command=callback)
lbltitle = ttk.Label(root, text='Title', font=(('Verdana'), 22))
lblname = ttk.Label(root, text="Your name :")
lblpass = ttk.Label(root, text='Your password :')

#Adjusting position
lbltitle.grid(row=0, column=0, columnspan=2, pady=10)
lblname.grid(row=1, column=0)
lblpass.grid(row=2, column=0)

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, pady=5)

chvar = IntVar()
chvar.set(0)


cbox = Checkbutton(root, text='Remeber your info', variable=chvar, font='Arial 16').grid(row=4, column=0)

#Gender check
gender = StringVar()

ttk.Radiobutton(root, text="Female", value="Female" , variable=gender).grid(row=5, column=0)
ttk.Radiobutton(root, text="Male", value="Male" , variable=gender).grid(row=5, column=1)

"""create combobox where our first parameter will be root
and the scond will be text variable(months) and use grid geometry manager
for the combobox (where it will be on the window)
when the application is run the combobox is empty
need to create variables for our combo box which we will do now"""
# there is a problem that when we run the program and click on a mon
# we can actually wite over it or delete it

months = StringVar()#StringVar is my function

ComboBox = ttk.Combobox(root, textvariable=months,
                          values= ('Jan', 'Feb', 'Mar','Apr',),
                          state='readonly').grid(row=6, column=0)
#tuple of values

#create spinbox-'from' is a special keyword for python-#
#so we need to use _after it.
year= StringVar()
spinbox(root, from_=1990, to=2022,text varable=year).grid(row=6,coloum=1)
#use grid geometry manager to our window
# but we are able to edit our values in the spin box
#Spinbox(root, from_=1990, to=2022, textvariable=year,
   #state ='readonly').grid(row=6, coulumn=1)
#to get the variable tom print out when program is run add a print statement in function 
#print (year.get())


#As always...
root.geometry('400x300')
root.mainloop()

