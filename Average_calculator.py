from tkinter import *

window = Tk()

window.title("Average Calculator")
window.geometry("600x800") #or other value
window.config(background = "black")


def calculate_average():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    num3 = float(entry3.get())
    average = (num1*1 + num2*1+num3*2) /4
    label = Label(window,
              text = f"Average:{average}", 
              font = ('Arial',22,'bold'), 
              fg='white', 
              bg= 'black' )
    label.place(x=35,y=200)
 


label = Label(window,
              text = "Basic Math 1", 
              font = ('Arial',23,'bold'), 
              fg='white', 
              bg= 'black' )
label.pack()

label_1 = Label(window, text ="1.0"+15*"  "+"1.0"+ 15*"  "+"2.0", font = ('Arial',20),fg='white', bg= 'black' )
label_1.pack()

entry1= Entry(window, width=5, font = ('Arial',20))
entry1.place(x=35, y=100)


entry2= Entry(window, width=5, font = ('Arial',20))
entry2.place(x=257, y=100)


entry3= Entry(window, width=5, font = ('Arial',20))
entry3.place(x=502, y=100)


button = Button(window, text="Calculate", font=('Arial', 25, 'bold'), command=calculate_average)
button.pack(side=BOTTOM)


window.mainloop()