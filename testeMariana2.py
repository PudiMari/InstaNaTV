from tkinter import *

from PIL import ImageTk, Image
from imageio.plugins import ffmpeg


class GameScreen:
    def __init__(self, master):
        # create all of the main containers
        top_left = Frame(master, bg='black', width=768, height=768)
        top_middle = Frame(master, bg='black', width=768, height=768)

        # layout all of the main containers
        top_left.grid(row=0, column=0)
        top_middle.grid(row=0, column=1)

        # create a canvas to show image on
        canvas_for_image = Canvas(top_left, bg='black', height=768, width=768, borderwidth=0, highlightthickness=0)
        canvas_for_image.grid(row=0, column=0, sticky='nesw', padx=0, pady=0)

        canvas_for_image2 = Canvas(top_middle, bg='black', height=768, width=768, borderwidth=0, highlightthickness=0)
        canvas_for_image2.grid(row=0, column=0, sticky='nesw', padx=0, pady=0)

        # create image from image location resize it to 200X200 and put in on canvas
        image = Image.open('bordadolistico/2021-06-19_18-56-05_UTC.jpg')
        image2 = Image.open('bordadolistico/2021-09-25_20-38-07_UTC.jpg')

        canvas_for_image.image = ImageTk.PhotoImage(image.resize((768, 768), Image.Resampling.LANCZOS))
        canvas_for_image.create_image(0, 0, image=canvas_for_image.image, anchor='nw')

        canvas_for_image2.image2 = ImageTk.PhotoImage(image2.resize((768, 768), Image.Resampling.LANCZOS))
        canvas_for_image2.create_image(0, 0, image=canvas_for_image2.image2, anchor='nw')

        input0 = 'bordadolistico/2021-05-08_15-51-38_UTC.mp4'
        input1 = 'bordadolistico/2021-09-25_20-38-07_UTC.mp4'

root = Tk()
root.title("Testando")
root.geometry("1536x864")
display = GameScreen(root)

root.mainloop()
