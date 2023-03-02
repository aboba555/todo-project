import customtkinter
from tkinter import *

window = customtkinter.CTk()
window.geometry("800x800")
window.resizable(False,False)
window.title("Todo")
customtkinter.set_appearance_mode("Light")


fot = customtkinter.CTkLabel(master=None,text="𝐓𝐨 𝐃𝐨",text_color="#6C8AFF",font=("",70))
fot.place(x=310,y=10)

fot = customtkinter.CTkLabel(master=None,text="𝐛𝐲 𝐚𝐛𝐨𝐛𝐚𝟓𝟓𝟓",text_color="#6C8AFF",font=("",35))
fot.place(x=580,y=610)


def add_item():
    if 60 < len(my_entry.get()):
        my_entry.delete(0,END)
    elif my_entry.get().isspace():
        my_entry.delete(0,END)
    else:
        my_list.insert(END,my_entry.get())
        my_entry.delete(0,END)

def setApperance():
    if setapperanceDark.get() == True:
        customtkinter.set_appearance_mode("Dark")
    else:
        customtkinter.set_appearance_mode("Light")


def delete_item():
    my_list.delete(ANCHOR)

def done_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg = "#3BE735")
    my_list.selection_clear(0,END)

def important_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#F14646")
    my_list.selection_clear(0,END)

my_frame = Frame(window)
my_frame.pack(pady=200)

my_entry = customtkinter.CTkEntry(window,font=("Helvetica",24),width=300)
my_entry.place(x=250,y=90)

add_btn = customtkinter.CTkButton(command=add_item,text="Add",master=None)
add_btn.place(x=630,y=165)

delete_btn = customtkinter.CTkButton(command=delete_item,text="Delete",master=None)
delete_btn.place(x=450,y=165)

done_btn = customtkinter.CTkButton(command=done_item,text="Done",master=None)
done_btn.place(x=250,y=165)

important_btn = customtkinter.CTkButton(command=important_item,text="Important",master=None)
important_btn.place(x=50,y=166)

setapperanceDark = customtkinter.CTkCheckBox(command=setApperance,text="Dark",master=None)
setapperanceDark.place(x=30,y=625)


my_list = Listbox(my_frame,
                  font=("Helvetica",30),
                  width = 45,
                  height=90,
                  bd = 0,
                  activestyle="none",
                  fg = "white",
                  highlightthickness=0,
                  selectbackground="#a6a6a6",
                  background="#353232")
my_list.pack()

my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)


window.mainloop()

