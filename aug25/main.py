from tkinter import *

window = Tk()
window.title("Miles to km converter")
window.minsize(width=500, height=700)
window.config(padx=10, pady=20)

miles_entry = Entry(width=30)
miles_entry.insert(END, string="Enter distance in miles")
miles_entry.grid(column=1, row=1)

# Labels
label = Label(text="Miles", font=("Arial", 12, "bold"))
label.grid(column=2, row=1)

is_equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_label.grid(column=0, row=2)

result_label = Label(text="0", font=("Arial", 12, "bold"))
result_label.grid(column=1, row=2)

label3 = Label(text="km", font=("Arial", 12, "bold"))
label3.grid(column=2, row=2)


def calc():
    miles = float(miles_entry.get())
    km = round(miles * 1.609)
    result_label.config(text=f"{km}")


button2 = Button(text="Calculate", command=calc)
button2.grid(column=1, row=3)

window.mainloop()
