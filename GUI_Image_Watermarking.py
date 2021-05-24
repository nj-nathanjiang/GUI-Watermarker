from PIL import Image
import tkinter as tk
from tkinter.filedialog import askopenfilename

DIRECTORY = "../Users/nathanj/Documents"


def open_image():
    open_button_text.set("Loading...")
    photo_name = askopenfilename(initialdir=DIRECTORY, title="Select A Photo To Watermark", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

    if photo_name:
        im = Image.open(photo_name).convert("RGBA")

        watermark = Image.open("watermark.png").convert("RGBA")
        watermark = watermark.resize((im.size[0], im.size[1]))
        watermark_mask = watermark.convert("RGBA")

        watermark_position = (im.size[0] - watermark.size[0], im.size[1] - watermark.size[1])
        new_im = Image.new("RGBA", im.size, (0, 0, 0, 0))
        new_im.paste(im, (0, 0))
        new_im.paste(watermark, watermark_position, mask=watermark_mask)

        finished_im = new_im.convert("RGB")
        finished_im_name = photo_name[:-4] + " watermarked.jpg"
        finished_im.save(finished_im_name)
        success_label_text.set("Image Watermark Successful")

        open_button_text.set("Browse")


screen = tk.Tk()
screen.title("Watermarking Program")

canvas = tk.Canvas(screen, width=750, height=600)
canvas.grid(columnspan=5, rowspan=5)


instructions_label = tk.Label(screen, text="Select a photo to watermark:")
instructions_label.grid(row=1, column=2)

open_button_text = tk.StringVar()
open_button_text.set("Select Photo")
open_button = tk.Button(screen, command=open_image, textvariable=open_button_text, height=2, width=15, bg="black")
open_button.grid(column=2, row=2)

success_label_text = tk.StringVar()
success_label_text.set(" ")
success_label = tk.Label(screen, textvariable=success_label_text)
success_label.grid(column=2, row=3)


screen.mainloop()
