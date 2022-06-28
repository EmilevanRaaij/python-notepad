from tkinter import *
from PIL import Image, ImageTk

window = Tk()
#----window settings----
title = "Notepad 2.0"
size = "490x500"
window.geometry(size)
font = "Arial"
main_icon = Image.open("C:/Users/emile/Pictures/photos/gui/journal_48px.png")
topbar_color = '#e8e8e8'
#-----------------------
window.title(title)
window.overrideredirect(1)
def follow_mouse(event):
    window.geometry("+{0}+{1}".format(event.x_root, event.y_root))
def hide_screen():
    window.overrideredirect(0)
    window.iconify()
def screen_appear(event):
    window.overrideredirect(1)
def quit():
   #action performed when you click the button quit and save
    global root
    with open("savetitle.txt", "w", encoding="utf-8") as file:
        for d in items:
            file.write(d + "\n")
    with open("savedescriptions.txt", "w", encoding="utf-8") as file:
        for d in descriptions:
            file.write(d + "\n")
    window.destroy()
exit_image = PhotoImage(file= "C:\\Users\emile\Pictures\photos\gui\close_window_32px.png")
minimize_image = PhotoImage(file= "C:\\Users\emile\Pictures\photos\gui\minimize_window_32px.png")
img = ImageTk.PhotoImage(main_icon.resize((16, 16)))
title_bar = Frame(window, bg= topbar_color, relief= SUNKEN, bd= 0)
top_icon = Label(title_bar, image= img, bg= topbar_color)
window_title = Label(title_bar, bg= topbar_color, text= title, font= "Arial 10", anchor= W)
exit_button = Button(title_bar, image= exit_image, bg= topbar_color, highlightbackground= "#a1a1a1", font= font, command= quit, height= 20, width= 20, borderwidth= 0)
minimize_button = Button(title_bar, image= minimize_image, bg= topbar_color, highlightbackground= "#a1a1a1", font= font, command= hide_screen, height= 20, width= 20, borderwidth= 0)
root = Frame(window, bg= '#b0b0b0', highlightthickness= 0)
#----functions and create widgets here----
listnum = 0
items = []
descriptions = []

def retrievedata():
    #Loads the data at the opening
    global items
    global descriptions
    items = []
    descriptions = []
    try:
        with open("savetitle.txt", "r", encoding="utf-8") as file:
            for f in file:
                list.insert(END, f.strip())
                items.append(f.strip())
                print(items)
    except:
        pass
    try:
        with open("savedescriptions.txt", "r", encoding="utf-8") as file:
            for f in file:
                descriptions.append(f.strip())
                print(descriptions)
    except:
        pass

def enter():
    global listnum
    global items
    global descriptions
    listnum = listnum + 1
    list.insert(listnum, titleinputfield.get())
    items.append(titleinputfield.get())
    descriptions.append("")
    titleinputfield.delete(first= 0, last= 100)
    print(items)
    print(descriptions)

def delete():
    global listnum
    global items
    global descriptions
    listnum = listnum - 1
    selection = list.curselection()
    list.delete(selection[0])
    items.pop(int(str(selection).strip("(,)")))
    descriptions.pop(int(str(selection).strip("(,)")))
    description.delete(1.0, END)
    
def save():
    selection = list.curselection()
    index = int(str(selection).strip("(,)"))
    descriptions[index] = description.get("1.0",'end-1c')
    print(items)
    print(descriptions)

def sel(evt):
    global descriptions
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    description.delete(1.0, END)
    description.insert(END, descriptions[index])

button_size = 32

add_image = Image.open("C:/Users/emile/Pictures/photos/gui/add_file_64px.png")
delete_image = Image.open("C:/Users/emile/Pictures/photos/gui/delete_file_64px.png")
save_image = Image.open("C:/Users/emile/Pictures/photos/gui/save_64px.png")

add_img = ImageTk.PhotoImage(add_image.resize((button_size, button_size)))
delete_img = ImageTk.PhotoImage(delete_image.resize((button_size, button_size)))
save_img = ImageTk.PhotoImage(save_image.resize((button_size, button_size)))

titleinputfield = Entry(root, font= "Arial 10 bold", width= 40, bg= "#949494", fg= 'white')
enterbutton = Button(root, image= add_img, font= "Arial 10 bold", command= enter, bg= "#b0b0b0")
deletebutton = Button(root, image= delete_img, font= "Arial 10 bold", command= delete, bg= "#b0b0b0")
savebutton = Button(root, image= save_img, font= "Arial 10 bold", command= save, bg= "#b0b0b0")
description = Text(root, font= "Arial 12", height= 22, width= 40, bg= "#f2f7bc", fg= '#000000')
list = Listbox(root, height= 23, width= 15, font= "Arial 10", bg= "#949494"
               ,highlightcolor= "#c2c2c2", highlightbackground= "#969696", selectbackground= "#c2c2c2", fg= 'white')
list.bind("<<ListboxSelect>>",sel)

#-----------------------------------------
title_bar.pack(expand= 1, fill= "x", side= TOP)
exit_button.pack(side= RIGHT, padx= 1, pady= 1)
minimize_button.pack(side= RIGHT, padx= 1, pady= 1)
root.pack(expand= 1, fill= "both")
top_icon.pack(side= LEFT, padx= 1, pady= 1)
window_title.pack(anchor= W)
#----position widgets here----

titleinputfield.grid(row= 0, column= 0, columnspan= 2, padx= 5, pady= 10)
enterbutton.grid(row= 0, column= 2, padx= 5, pady= 10)
savebutton.grid(row= 0, column= 3, padx= 5, pady= 10)
deletebutton.grid(row= 0, column= 4, padx= 5)
description.grid(row= 1, column= 1, columnspan= 4)
list.grid(row= 1, column= 0, pady= 10, padx= 5)

#-----------------------------
window_title.bind('<B1-Motion>', follow_mouse)
top_icon.bind('<B1-Motion>', follow_mouse)
title_bar.bind('<B1-Motion>', follow_mouse)
title_bar.bind("<Map>", screen_appear)

retrievedata()
window.mainloop()