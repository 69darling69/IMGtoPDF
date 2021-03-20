import sys
import tkinter

from PIL import Image, UnidentifiedImageError  # Не родной
from fpdf import FPDF  # Не родной
from tkinter import filedialog, ttk, messagebox


root = tkinter.Tk()
root.title('IMGtoPDF')

root.withdraw()
Images = filedialog.askopenfilenames()
root.deiconify()

pdf = FPDF()
Label = tkinter.Label(root)
Label.pack()
Bar = ttk.Progressbar(root, maximum=len(Images), value=0)
Bar.pack()
root.update()
for image in Images:
    Label['text'] = image
    root.update()
    try:
        io = Image.open(image)
        scaleSize = (210, io.size[1] / io.size[0] * 210)
    except UnidentifiedImageError:
        messagebox.showerror('Error', image + ' is not an image')
        sys.exit()
    pdf.add_page()
    pdf.image(image, 0, 0, *scaleSize)
    Bar['value'] += 1
    root.update()
try:
    SavePath = filedialog.asksaveasfile(filetypes=[('PDF', '*.pdf')]).name
    pdf.output(SavePath, 'F')
except AttributeError:
    pass

sys.exit()
