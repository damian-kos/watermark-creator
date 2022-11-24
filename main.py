from tkinter import *
from tkinter import filedialog, Text
import PIL.Image
import PIL.ImageTk
import PIL.ImageFont
import PIL.ImageDraw

TEXT = ""
MYIMG = None
IM2 = None
images = []
files = []
open_images = []
CURRENTLY_OPEN_IMAGE = None

# Initialize main window
window = Tk()
window.geometry("1400x1000")
window.config(padx=15, pady=15)

# Left side of main window. Contains text, images, input files
left_frame = Frame(window)
left_frame.grid(column=0, row=0, pady=80)

# Right side of main windows. Display images and text which we want to
# put as watermark.
right_frame = Frame(window)
right_frame.grid(column=1, row=0)

# Creates placeholder for images to display on right_frame.
canvas = Canvas(right_frame, width=350, height=350, bg="white")
image_container = canvas.create_image(0, 0, anchor=NW)
canvas.grid(
    padx=50,
)

# Frame within left_frame. Displays text instructions.
text_frame = Frame(left_frame)
text_frame.grid(column=0)

# Text instructions how to use program.
texts = [
    "Add a watermark to your photos:",
    "1. Please select a watermark. For best results choose PNG file.",
    "2. Then select the images you want to add"
    " the watermark to!",
    "3. You can see a preview by clicking on image in the list.",
    "4. Finally you can change the position and settings of the"
    " watermark with the options below.",
    "5. Once you are happy with results, click 'Save' to save your work.",
]

for text in texts:
    Label(text_frame, text=text).grid(column=1)

# Global TEXT variable input field.
watermark_text = Text(text_frame, width=40, height=1)
watermark_text.grid(column=0, columnspan=2)

# Frame for buttons in left_frame. They are used to get data from input
# and display text on image place.
text_buttons_frame = Frame(left_frame)
text_buttons_frame.grid(padx=10, pady=10)


# Responsible for displaying TEXT with given parameters.


def show_text(opacity=255, x=0, y=0):
    """
    Shows and updates watermark text. Takes opacity, x axis and y axis
    as arguments.
    """
    global MYIMG, IM2
    if TEXT != "":

        # Defines font which will be used.
        font = PIL.ImageFont.truetype("arial.ttf", 48)
        # Creates and displays TEXT we given earlier with parameters
        # opacity, x and y we set on sliders. Text area size
        text_bg = PIL.Image.new(
            "RGBA", CURRENTLY_OPEN_IMAGE.size, (0, 0, 0, 0))
        draw_text_bg = PIL.ImageDraw.Draw(text_bg)
        draw_text_bg.text(
            (0, 0), TEXT, (255, 255, 255, int(opacity_slider.get())), font=font
        )
        IM2 = PIL.Image.new("RGBA", CURRENTLY_OPEN_IMAGE.size, (0, 0, 0, 0))
        IM2.paste(
            text_bg,
            (x_axis_location.get(), y_axis_location.get()),
            mask=text_bg.convert("RGBA"),
        )
        MYIMG = PIL.ImageTk.PhotoImage(IM2)
        canvas.create_image(0, 0, image=MYIMG, anchor="nw")


Button(text_buttons_frame, text="Convert", command=show_text).grid(
    column=1, row=1, padx=10
)


def retrieve_input():
    """ Retrieves a text which is input by user in Text field."""
    global TEXT
    TEXT = watermark_text.get("1.0", END)


Button(text_buttons_frame, text="Get text", command=retrieve_input).grid(
    column=0, row=1, padx=10
)


sliders_frame = Frame(left_frame)
sliders_frame.grid(column=0)


def update_opacity(opacity):
    """ Updates opacity with value given in Scale opacity_slider"""
    show_text(opacity=opacity)


opacity_slider = Scale(
    sliders_frame,
    label="Opacity",
    from_=0,
    to=255,
    command=update_opacity,
    orient=HORIZONTAL,
)
opacity_slider.grid(column=1, row=0)


def update_x_axis(x):
    """ Updates watermark text location in X axis with value given
    in Scale x_axis_location"""
    show_text(x=x)


x_axis_location = Scale(
    sliders_frame,
    label="X Axis",
    from_=0,
    to=350,
    command=update_x_axis,
    orient=HORIZONTAL,
)
x_axis_location.grid(column=0, row=1)


def update_y_axis(y):
    """ Updates watermark text location in Y axis with value given
    in Scale y_axis_location"""
    show_text(y=y)


y_axis_location = Scale(
    sliders_frame,
    label="Y Axis",
    from_=0,
    to=350,
    command=update_y_axis,
    orient=HORIZONTAL,
)
y_axis_location.grid(column=3, row=1)


files_frame = Frame(left_frame)
files_frame.grid()


def get_local_file():
    """ Opens file/s from chosen folder. """
    file_path = filedialog.askopenfilename(multiple=True)
    # Takes chosen files path and formats it to, so only filename is left.
    for file in file_path:
        file_name = file.split("/")[-1::]
        files.append(file_name)
    # Inputs these names in a listbox which displays them for user.
    # They can be accesed by a click.
    for file_name in files:
        images_listbox.insert("end", file_name)
    for file_image in files:
        open_images.append(PIL.ImageTk.PhotoImage(
            PIL.Image.open(f"images/{file_image[0]}")))


def print_filename(event):
    """ Displays chosen image from listbox in canvas. """
    global CURRENTLY_OPEN_IMAGE
    # Defines which image is chosen.
    image_index = images_listbox.curselection()[0]
    # Opens image.
    CURRENTLY_OPEN_IMAGE = PIL.Image.open(f"images/{files[image_index][0]}")
    # Setup canvas size to a size of opened image.
    canvas_size = CURRENTLY_OPEN_IMAGE.size
    x_axis_location.configure(to=canvas_size[0])
    y_axis_location.configure(to=canvas_size[1])
    canvas.config(width=canvas_size[0], height=canvas_size[1])
    canvas.itemconfig(image_container, image=open_images[image_index])
    canvas.update()


# Create listbox where images will be listed.
images_listbox = Listbox(files_frame, width=90, height=10)
images_listbox.grid(column=1, row=1, sticky=(N, W, E, S))

# Add scrollbar on the left of images_listbox.
images_listbox_scrollbar = Scrollbar(
    files_frame, orient=VERTICAL, command=images_listbox.yview
)
images_listbox_scrollbar.grid(column=0, row=1, stick=NS)
images_listbox["yscrollcommand"] = images_listbox_scrollbar.set

images_listbox.bind("<<ListboxSelect>>", print_filename)

Button(files_frame, text="Chose your file", command=get_local_file).grid(
    column=1, pady=10
)
Button(files_frame, text="Quit", command=window.destroy).grid(column=1)


def save_image():
    """ Saves image with watermark we have currently
    displaying in canvas"""
    final_image = PIL.Image.new("RGBA", CURRENTLY_OPEN_IMAGE.size)
    final_image.paste(CURRENTLY_OPEN_IMAGE)
    final_image.paste(IM2, (0, 0), mask=IM2.convert("RGBA"))
    final_image.save("final.png")


Button(files_frame, text="Save results", command=save_image).grid(column=1)


window.mainloop()
