from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("To-Do List")
root.geometry("500x500")

my_font = Font(family="Georgia", size=20, weight="bold")

my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(my_frame, font=my_font, width=25, height=5, bg="SystemButtonFace", bd=0,
                  fg="#464646", highlightthickness=0, selectbackground="#a6a6a6", activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

stuff = ["Good Morning", "Get your Breakfast", "Get Ready", "Lunch", "Come Home"]
for item in stuff:
    my_list.insert(END, item)

my_entry = Entry(root, font=("Georgia", 18))
my_entry.pack(pady=10)

button_frame = Frame(root)
button_frame.pack(pady=10)

def delete_item():
    selected = my_list.curselection()
    if selected:
        my_list.delete(selected[0])

def add_item():
    task = my_entry.get().strip()
    if task:
        my_list.insert(END, task)
        my_entry.delete(0, END)

def cross_off_item():
    selected = my_list.curselection()
    if selected:
        for item in selected:
            my_list.itemconfig(item, fg="gray", selectbackground="gray")

def uncross_off_item():
    selected = my_list.curselection()
    if selected:
        for item in selected:
            my_list.itemconfig(item, fg="#464646", selectbackground="#a6a6a6")

delete_button = Button(button_frame, text="Delete", command=delete_item, width=12)
add_button = Button(button_frame, text="Add", command=add_item, width=12)
cross_off_button = Button(button_frame, text="Cross Off", command=cross_off_item, width=12)
uncross_off_button = Button(button_frame, text="Uncross Off", command=uncross_off_item, width=12)

delete_button.grid(row=0, column=0, padx=5, pady=5)
add_button.grid(row=0, column=1, padx=5, pady=5)
cross_off_button.grid(row=0, column=2, padx=5, pady=5)
uncross_off_button.grid(row=0, column=3, padx=5, pady=5)

root.mainloop()
