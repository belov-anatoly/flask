# подключаем элементы tkinter (PyQt5)
import os
from datetime import datetime
from tkinter import CENTER, LEFT, NW, N, X, TOP
from tkinter import Tk, PhotoImage, Label, Canvas, Button
from tkinter import filedialog  # для выбора картинки
from PIL import Image, ImageTk, ImageFilter, ImageEnhance  # для обработки изображений


class App():
    def __init__(self):
        self.window = Tk()  # создали окно
        self.window.title('Обработка картинок')
        self.window.geometry('800x600')
        self.window.resizable(False, False)
        self.window.iconphoto(False, PhotoImage(file='pencil.png'))
        self.apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
        self.label = Label(text='Обработка изображений',
                           background='#ffff00', foreground='red',
                           font=('Verdana', 16))
        self.label.pack(fill=X, pady=5)
        self.canvas = Canvas(bg='white', width=600, height=400)
        self.canvas.pack(anchor=CENTER, pady=20)
        self.load = Button(text='Открыть', command=self.open)
        self.load.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.blur = Button(text='Размыть', command=self.blur)
        self.blur.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.sharp = Button(text='Резкость', command=self.sharp)
        self.sharp.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.dtime = Label(background='#ffffff', foreground='#111111',
                           font=('Verdana', 26))
        self.dtime.place(x=310, y=530)
        self.cwd = os.getcwd()
        self.image = None  # заглушка
        self.orig = Image.new('RGB', (600, 400), (255, 255, 255))
        self.show_time()
        self.window.mainloop()  # ожидание

    def open(self):
        try:
            fullpath = filedialog.askopenfilename(title='Выбор картинки',
                                                  initialdir=self.cwd,
                                                  filetypes=(
                                                      ('GIF', '*.gif'),
                                                      ('PNG', '*.png'),
                                                      ('JPG', '*.jpg')
                                                  )
                                                  )
            self.orig = Image.open(fullpath)
            self.w, self.h = self.orig.size
            mode = self.orig.mode
            if mode == 'P':  # Если 256 color indexed image
                self.orig = self.orig.convert('RGB')
            if self.w > 600:
                ratio = self.w / 600
                self.orig = self.orig.resize((600, int(self.h / ratio)))
            self.image = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        except AttributeError:
            self.image = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    def blur(self):
        blur_image = self.orig.filter(ImageFilter.BLUR)
        self.image = ImageTk.PhotoImage(blur_image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    def sharp(self):
        sharper = ImageEnhance.Sharpness(self.orig)
        sharp_img = sharper.enhance(5.0)
        self.image = ImageTk.PhotoImage(sharp_img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    def show_time(self):
        self.time_to_show = datetime.time(datetime.now()).strftime("%H:%M:%S")
        self.dtime['text'] = self.time_to_show
        self.dtime.after(1000, self.show_time)


if __name__ == '__main__':
    app = App()
