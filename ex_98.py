from tkinter import *

lst = []

root = Tk()
root.title("Simple GUI Application")
root.geometry('400x40')

txt = Entry(root, width=25, font=('Arial 12'))
txt.grid(column=1, row=0)


def add_line():
    entered_data = txt.get()
    lst.append(entered_data)
    txt.delete(0, END)

def save():
    global lst
    with open("demo_data.txt", "a+") as file:
        for line in lst:
            file.write(line+"\n")
    txt.insert(0, "")
    lst = []
    

def save_and_close():
    global lst
    with open("demo_data.txt", "a+") as file:
        for line in lst:
            file.write(line+"\n")
    root.destroy()


add_line_btn = Button(root, text = "Add Line", command = add_line)
add_line_btn.grid(column=2, row=0)

save_btn = Button(root, text = "Save", command = save)
save_btn.grid(column=4, row=0)

save_and_close_btn = Button(root, text = "Save and Close", command = save_and_close)
save_and_close_btn.grid(column=5, row=0)


root.mainloop()