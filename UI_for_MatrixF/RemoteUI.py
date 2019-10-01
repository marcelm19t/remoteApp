# Author MAMA | 01.10.2019

import socket

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

from tkinter import Tk


RASP_IP = '192.168.1.1'
RASP_PORT = 5005


def get_id(instance):
    for identification, widget in instance.parent.ids.items():
        if widget.__self__ == instance:
            return identification


class MainWidget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((RASP_IP, RASP_PORT))

    def __del__(self):
        self.clientsocket.close()

    @staticmethod
    def button_pressed(instance):
        print(int(get_id(instance).lstrip('n')))

    @staticmethod
    def tubing_set(instance):
        print(instance.text)

    @staticmethod
    def mode_switched(instance):
        print(instance.text)


class RemoteApp(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    Window.fullscreen = True
    Window.size = (width, height)
    RemoteApp().run()
