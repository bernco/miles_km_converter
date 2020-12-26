from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(height=200, width=200)
window.config(padx=20, pady=20)


# function to calculate
def calculate():
    input_val = miles_text.get(1.0, END)
    input_val_int = int(input_val)
    result = round(input_val_int*1.609344)
    result_label.config(text=f"{result}")


# conversion label
conv_label = Label(text="is equal to")
conv_label.grid(column=1, row=2)
conv_label.config(padx=10, pady=10)

# digit text entry
miles_text = Text(width=5, height=1)
miles_text.grid(column=2, row=1)
miles_text.config(padx=5, pady=5)

# miles label
miles_label = Label(text="miles")
miles_label.grid(column=3, row=1)
miles_label.config(padx=10, pady=10)

# result label
result_label = Label(text="0")
result_label.grid(column=2, row=2)
result_label.config(padx=10, pady=10)

# km label
km_label = Label(text="Km")
km_label.grid(column=3, row=2)
km_label.config(padx=10, pady=10)

# calculate button
calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=2, row=3)
calc_button.config(padx=3, pady=3)

window.mainloop()
