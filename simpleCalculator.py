#Tyler Fisher
#01/06/25 
#Simple Calculator
from tkinter import * 
from tkinter import ttk
#inputs/variables 
userInput1 = 0
userInput2 = 0
index = 0
symbol = "A"
#Pressing the number keys function
def numPress(x):
    global userInput1
    global userInput2
    global index
    if index == 0:
        str1 = str(userInput1)
        str2 = str(x)
        str3 = str1 + str2
        userInput1 = int(str3)
        ttk.Label(frm, text=userInput1, background="lightgrey", anchor="e").grid(column=1, row=0, columnspan=3, sticky=NSEW)
    else: 
        str1 = str(userInput2)
        str2 = str(x)
        str3 = str1 + str2
        userInput2 = int(str3)
        ttk.Label(frm, text=userInput2, background="lightgrey", anchor="e").grid(column=1, row=0, columnspan=3, sticky=NSEW)
#Pressing the arithmetic and button keys function
def symbolPress(x):
    global index
    global symbol 
    global userInput1
    global userInput2
    if x != "=":
        index += 1
        symbol = x
    else:
        match symbol:
            case "+":
                result = (userInput1 + userInput2) 
                ttk.Label(frm, text=result, background="lightgrey", anchor="e").grid(column=1, row=0, columnspan=3, sticky=NSEW)
            case "-":
                result = (userInput1 - userInput2)
                ttk.Label(frm, text=result, background="lightgrey", anchor="e").grid(column=1, row=0, columnspan=3, sticky=NSEW) 
            case "/":
                result = (userInput1 / userInput2)
                ttk.Label(frm, text=result, background="lightgrey", anchor="e").grid(column=1, row=0, columnspan=3, sticky=NSEW)
            case "*":
                result = (userInput1 * userInput2)
                ttk.Label(frm, text=result, background="lightgrey", anchor="e").grid(column=1, row=0, columnspan=3, sticky=NSEW) 
        userInput1 = 0
        userInput2 = 0
        index = 0
#UI 
root = Tk()
frm = ttk.Frame(root, padding =50)
frm.grid()
ttk.Label(frm, text="Simple Calculator").grid(column=0, row=0)
ttk.Label(frm, text="0", background="lightgrey", anchor="e").grid(column=1, row=0, columnspan=3, sticky=NSEW)
#The Number buttons
ttk.Button(frm, text="7" , command=lambda: numPress(7)).grid(column=1, row=1)
ttk.Button(frm, text="8" , command=lambda: numPress(8)).grid(column=2, row=1)
ttk.Button(frm, text="9" , command=lambda: numPress(9)).grid(column=3, row=1)
ttk.Button(frm, text="4" , command=lambda: numPress(4)).grid(column=1, row=2)
ttk.Button(frm, text="5" , command=lambda: numPress(5)).grid(column=2, row=2)
ttk.Button(frm, text="6" , command=lambda: numPress(6)).grid(column=3, row=2)
ttk.Button(frm, text="1" , command=lambda: numPress(1)).grid(column=1, row=3)
ttk.Button(frm, text="2" , command=lambda: numPress(2)).grid(column=2, row=3)
ttk.Button(frm, text="3" , command=lambda: numPress(3)).grid(column=3, row=3)
ttk.Button(frm, text="0" , command=lambda: numPress(0)).grid(column=2, row=4)
#The Arithmetic buttons
ttk.Button(frm, text="+", command=lambda: symbolPress("+")).grid(column=4, row=0)
ttk.Button(frm, text="-", command=lambda: symbolPress("-")).grid(column=4, row=1)
ttk.Button(frm, text="/", command=lambda: symbolPress("/")).grid(column=4, row=2)
ttk.Button(frm, text="*", command=lambda: symbolPress("*")).grid(column=4, row=3)
#Equal Button 
ttk.Button(frm, text="=", command=lambda: symbolPress("=")).grid(column=4, row=4)
#start main loop
root.mainloop()
#Exit message
print("Good Bye!")