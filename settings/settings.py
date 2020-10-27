import pygame
import json
import pyautogui as pug

class Settings:

    def __init__(self):
        self.file_path = 'data/data.json'
        self.screen_size = pug.size()
        self.fullscreen = True
        self.resolution = [1280, 720]
        self.fps = 0

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

        self.fullscreen = data['settings']['fullscreen']['value']
        self.resolution = data['settings']['resolution']['value']
        self.fps = data['settings']['fps']['value']

        # Load controls
        for i in self.controls:
            self.controls[i] = data['settings']['controls'][i]['value']

    def wow3(self, var, name, data):
        data['settings'][name]  = {}
        data['settings'][name]['value'] = var

    def save(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        data['settings'] = {}

        # Save variables
        self.wow3(self.fullscreen, 'fullscreen', data)
        self.wow3(self.resolution, 'resolution', data)
        self.wow3(self.fps, 'fps', data)

        # Save Controls Dict
        data['settings']['controls'] = {}
        for i in self.controls:
            data['settings']['controls'][i] = {}
            data['settings']['controls'][i]['value'] = self.controls[i]

        with open(self.file_path, 'w') as f:
            json.dump(data, f)
