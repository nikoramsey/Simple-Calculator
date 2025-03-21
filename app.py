import tkinter as tk 

# Funtion to handle button clicks 
def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))

# Funtion to calculate the result 
def calculate():
    try:
        result = eval(entry_var.get())  #Evaluates the expression (e.g 5+3)
        entry_var.set(result)
    except Exception:
        entry_var.set("Error")

# Funtion to clear the entry
def clear():
    entry_var.set("")

# Create a main window
root =  tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Create a variable to hold the entry text
entry_var = tk.StringVar()

# Entry field (Display screen)
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

# Button layout
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial",20), command=calculate, width=5, height=2)
    else:
        btn = tk.Button(root, text=text, font=("Arial",20), command=lambda t=text: on_button_click(t), width=5, height=2)
    btn.grid( row=row, column=col)

# Clear button
clear_btn = tk.Button(root, text="C", font=("Arial",20), command=clear, width=21, height=2)
clear_btn.grid(row=5, column=0, columnspan=4)

#Run the GUI app
root.mainloop()
