from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget example")
window.minsize(width=400, height=600)

# Labels
label = Label(text="This is an old text")
label.config(text="This is a newer text")
label.pack()


# Buttons
def action():
    print("Button action")
    new_text = entry.get()
    label.config(text=new_text)


# calls action when pressed
button = Button(text="Click Me", command=action)
button.pack()

# Entries
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with")
entry.pack()

# Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=100, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used():
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
checked_state1 = IntVar()
checked_state2 = IntVar()

checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton1 = Checkbutton(text="Is On?", variable=checked_state1, command=checkbutton_used)
checkbutton2 = Checkbutton(text="Is On?", variable=checked_state2, command=checkbutton_used)
checked_state.get()
checkbutton.pack()
checkbutton1.pack()
checkbutton2.pack()

# RadioButton

def radiobutton_checked():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radiobutton_checked)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radiobutton_checked)
radiobutton3 = Radiobutton(text="Option3", value=3, variable=radio_state, command=radiobutton_checked)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

# Listbox

def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
