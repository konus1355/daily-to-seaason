from tkinter import *
from tkinter import font

root = Tk()
root.title("Season-long to Max daily catch converter")
root.geometry("400x250")
root.iconbitmap('favicon.ico')

# Font and padding settings
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=12)
root.option_add("*Font", default_font)
pad_x = 10
pad_y = 5

# Input
label1 = Label(root, text="Season-long catch")
label1.grid(row=0, column=0, padx=pad_x, pady=pad_y)
entry1 = Entry(root, width=10)
entry1.grid(row=0, column=1, padx=pad_x, pady=pad_y)

label2 = Label(root, text="Flight in Weeks")
label2.grid(row=1, column=0, padx=pad_x, pady=pad_y)
entry2 = Entry(root, width=10)
entry2.grid(row=1, column=1, padx=pad_x, pady=pad_y)

# Functions
def calculate():
    convert1 = entry1.get()
    convert2 = entry2.get()
    a = int(convert1)
    x = int(convert2)
    answer1 = a / (2.87 * x)
    answer2 = a / (0.96 * x)
    finalans1 = round(answer1,2)
    finalans2 = round(answer2,2)
    anslabel.config(text=str(finalans1) + "-" + str(finalans2))

def about():
    winx = root.winfo_x()
    winy = root.winfo_y()
    about_win = Toplevel(root)
    about_win.title("About")
    about_win.geometry("+%d+%d" % (winx + 50, winy + 50))
    abt_label1 = Label(about_win, text="Programmed by: Andrei Onufriev")
    abt_label1.grid(row=0, column=0, columnspan=2, pady=pad_y)
    abt_label2 = Label(about_win, text="2020 ©")
    abt_label2.grid(row=1, column=0, pady=pad_y)
    abt_label3 = Label(about_win, text="Onufrieva, K. S. & A. V. Onufriev. 2018. Linear relationship between peak and season-long abundances in insects. PLOS ONE 13: e0193110.doi:10.1371/journal.pone.0193110.")
    abt_label3.grid(row=2, column=0, columnspan=2, pady=pad_y)
    about_win.iconbitmap('favicon.ico')

# Buttons
button1 = Button(root, text="Calculate", command=calculate, width=12)
button1.grid(row=2, column=0, columnspan=2, pady=(10, 5))
button2 = Button(root, text="About", command=about, width=12)
button2.grid(row=3, column=0, columnspan=2, pady=5)

# Output
output_label = Label(root, text="Output Range:")
output_label.grid(row=4, column=0, padx=pad_x, pady=pad_y)
anslabel = Label(root, text="")
anslabel.grid(row=4, column=1, padx=pad_x, pady=pad_y)

root.mainloop()
