import pygame
import json
import pyautogui as pug

class Settings:

    def __init__(self):
        self.file_path = 'data/settings.json'
        self.screen_size = [1280, 720] # pug.size()
        self.fullscreen = False
        self.resolution = [1280, 720]
        self.fps = 60

        self.controls = {

            'up': 'w',
            'left': 'a',
            'down': 's',
            'right': 'd',
            'dodge': 'space'

        }

    def load(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        self.fullscreen = data['fullscreen']['value']
        self.resolution = data['resolution']['value']
        self.fps = data['fps']['value']

        # Load controls
        for i in self.controls:
            self.controls[i] = data['controls'][i]['value']

    def wow3(self, var, name, data):
        data[name] = {}
        data[name]['value'] = var

    def save(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        # Save variables
        self.wow3(self.fullscreen, 'fullscreen', data)
        self.wow3(self.resolution, 'resolution', data)
        self.wow3(self.fps, 'fps', data)

        # Save Controls Dict
        data['controls'] = {}
        for i in self.controls:
            data['controls'][i] = {}
            data['controls'][i]['value'] = self.controls[i]

        with open(self.file_path, 'w') as f:
            json.dump(data, f)
