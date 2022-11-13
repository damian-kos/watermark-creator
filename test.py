from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import PIL.Image, PIL.ImageTk, PIL.ImageFont, PIL.ImageDraw

TEXT = ""

window = Tk()
window.geometry("1000x800")
window.config(padx=15, pady=15)
images = []

frm = Frame(window)
frm.grid()


Label(frm, text="Add a watermark to your photos:").grid(column=1, columnspan=2, row=0, pady=100)
Label(frm, text="1. Please select a watermark. For best results choose PNG file.").grid(column=1, columnspan=2,row=1)
Label(frm, text="2. Then select the images you want to add the watermark to!").grid(column=1, columnspan=2,row=2)
Label(frm, text="3. You can see a preview by cliking on image in the list").grid(column=1, columnspan=2,row=3)
Label(frm, text="4. Finally you can change the position and settings of the watermark with the options below.").grid(column=1, columnspan=2,row=4)
Label(frm, text="5. Once you are happy with results, click 'Save' to save your work.").grid(column=1, columnspan=2,row=5)


# Text watermark

watermark_text = Text(frm, width=40, height=1)
watermark_text.grid(column=1, row=6)

def retrieve_input():
    global TEXT
    TEXT = watermark_text.get('1.0', END)
   
get_text = Button(frm, text="Get text", command=retrieve_input).grid(column=1, row=7)


    


files = []

def get_local_file():
    root=tk.Tk()
    root.withdraw()

    file_path=filedialog.askopenfilename(multiple=True)
    for file in file_path:
        file_name = file.split("/")[-1::]
        files.append(file_name)
    for i in files:
        images_listbox.insert('end', i)

def print_filename(event):
    image_index = images_listbox.curselection()[0]
    image_to_edit = files[image_index][0]

    myimg = PIL.ImageTk.PhotoImage(PIL.Image.open(f"images/{image_to_edit}").resize((350, 350)))
    img_label = Label(image=myimg)
    img_label.image = myimg
    img_label.grid(column=2, row=0, padx=50)


images_listbox = Listbox(frm, width=90, height=10)
images_listbox.grid(column=1, row=8,  sticky=(N,W,E,S))

for i in files:
    images_listbox.insert('end', i)

images_listbox_scrollbar = Scrollbar(frm, orient=VERTICAL, command=images_listbox.yview)
images_listbox_scrollbar.grid(column=0, row=8, stick=NS)
images_listbox['yscrollcommand'] = images_listbox_scrollbar.set

images_listbox.bind("<<ListboxSelect>>", print_filename)

Button(frm, text="Chose your file", command=get_local_file).grid(column=1, row=9)
Button(frm, text="Quit", command=window.destroy).grid(column=1, row=10)


def show_text():
    if TEXT != "":
        print(TEXT[0])
        im2 = PIL.Image.new("RGBA", (200, 200), (255,255,255,0))
        font = PIL.ImageFont.truetype("arial.ttf", 48)
        d = PIL.ImageDraw.Draw(im2)
        d.text((100, 100), TEXT, fill=(255, 255, 255, 200), anchor="ms", font=font)

        myimg = PIL.ImageTk.PhotoImage(im2)
        # myimg = im2
        img_label = Label(image=myimg)
        img_label.image = myimg
        img_label.grid(column=2, row=0, padx=50)



Button(frm, text="Convert", command=show_text).grid(column=1, row=11)


window.mainloop()


