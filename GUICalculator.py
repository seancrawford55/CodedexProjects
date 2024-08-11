#Python GUI Calculator
from tkinter import *

#Start with a blank expression
exp = ''

def press(num):
    global exp
    #concat the string in the window
    exp = exp + str(num)
    equation.set(exp)  # type: ignore


def equalPress():
    try:
        global exp

        total = str(eval(exp))
        equation.set(total) # type: ignore

        exp = ''
    except:
        equation.set('Error') # type: ignore
        exp = ''

def clear():
    global exp
    exp = ''
    equation.set('')# type: ignore

if __name__ == "__main__":
    gui = Tk()

    #set title 
    gui.title("Calculator")

    #set background color
    gui.configure(background="Blue")

    #set size of window
    gui.geometry('500x450')

    equation = StringVar()

    #text entry for the expression
    exp_field = Entry(gui, textvariable=equation)

    exp_field.grid(columnspan = 10, ipadx = 100)

    button1 = Button(gui, text=' 1 ', fg='black', bg='green', 
                    command=lambda: press(1), height=5, width=15) 
    button1.grid(row=2, column=0) 
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='green', 
                    command=lambda: press(2), height=5, width=15) 
    button2.grid(row=2, column=1) 
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='green', 
                    command=lambda: press(3), height=5, width=15) 
    button3.grid(row=2, column=2) 
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='green', 
                    command=lambda: press(4), height=5, width=15) 
    button4.grid(row=3, column=0) 
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='green', 
                    command=lambda: press(5), height=5, width=15) 
    button5.grid(row=3, column=1) 
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='green', 
                    command=lambda: press(6), height=5, width=15) 
    button6.grid(row=3, column=2) 
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='green', 
                    command=lambda: press(7), height=5, width=15) 
    button7.grid(row=4, column=0) 
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='green', 
                    command=lambda: press(8), height=5, width=15) 
    button8.grid(row=4, column=1) 
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='green', 
                    command=lambda: press(9), height=5, width=15) 
    button9.grid(row=4, column=2) 
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='green', 
                    command=lambda: press(0), height=5, width=15) 
    button0.grid(row=5, column=0) 
 
    plus = Button(gui, text=' + ', fg='black', bg='green', 
                command=lambda: press("+"), height=5, width=15) 
    plus.grid(row=2, column=3) 
 
    minus = Button(gui, text=' - ', fg='black', bg='green', 
                command=lambda: press("-"), height=5, width=15) 
    minus.grid(row=3, column=3) 
 
    multiply = Button(gui, text=' * ', fg='black', bg='green', 
                    command=lambda: press("*"), height=5, width=15) 
    multiply.grid(row=4, column=3) 
 
    divide = Button(gui, text=' / ', fg='black', bg='green', 
                    command=lambda: press("/"), height=5, width=15) 
    divide.grid(row=5, column=3) 
 
    equal = Button(gui, text=' = ', fg='black', bg='green', 
                command=equalPress, height=5, width=15) 
    equal.grid(row=5, column=2) 
 
    clear = Button(gui, text='Clear', fg='black', bg='green', 
                command=clear, height=5, width=15) 
    clear.grid(row=5, column='1') 
 
    Decimal= Button(gui, text='.', fg='black', bg='green', 
                    command=lambda: press('.'), height=5, width=15) 
    Decimal.grid(row=6, column=0) 

    gui.mainloop()