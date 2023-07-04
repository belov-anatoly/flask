# подключаем элементы tkinter (PyQt5)
import os
import requests
from io import BytesIO
from tkinter import CENTER, LEFT, NW, N, X
from tkinter import Tk, PhotoImage, Label, Canvas, Button, Entry
from PIL import Image, ImageTk  # для обработки изображений


class App:
    def __init__(self):
        self.window = Tk()  # создали окно
        self.window.title('Поиск по карте')
        self.window.geometry('800x600')
        self.window.resizable(False, False)
        self.window.iconphoto(False, PhotoImage(file='pencil.png'))
        self.apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
        self.name = 'СПб, Можайская, 2'
        self.geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey={self.apikey}' \
                                f'&geocode={self.name}&kind=metro&format=json'
        self.label = Label(text='Поиск по карте',
                           background='#ffff00', foreground='red',
                           font=('Verdana', 16))
        self.label.pack(fill=X, pady=5)
        self.canvas = Canvas(bg='white', width=600, height=450)
        self.canvas.pack(anchor=CENTER, pady=20)
        self.load = Button(text='Найти', command=self.open)
        self.load.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.place = Entry(width=60, font=('Verdana', 16))
        self.place.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.cwd = os.getcwd()
        self.image = None  # заглушка
        self.orig = Image.new('RGB', (600, 400), (255, 255, 255))
        self.window.mainloop()  # ожидание

    def open(self):
        self.name = self.place.get()
        if self.name == '' or len(self.name) < 5:
            self.name = 'СПб, Можайская, 2'
        self.geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey={self.apikey}&geocode={self.name}' \
                                f'&kind=metro&format=json'
        response = requests.get(self.geocoder_request)
        info = response.json()
        coords = info['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        coords = ','.join(coords.split())
        delta = '0.0005,0.0005'
        # собираем параметры для запроса к static-maps
        map_param = {
            'll': coords,
            'spn': delta,
            'l': 'map',
            'pt': f'{coords},pm2dgl'
        }
        api_server = 'https://static-maps.yandex.ru/1.x/'
        image_map = requests.get(api_server, params=map_param)
        pict_to_show = Image.open(BytesIO(image_map.content))
        self.image = ImageTk.PhotoImage(pict_to_show)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)


if __name__ == '__main__':
    app = App()
