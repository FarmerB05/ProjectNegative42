import json
from item.sword import Sword
import pygame
from convert.convert import str_2_item

# Just a thought, I don't know how much it will help, use sepret json files for faster loading.
# Only if it becomes a problem, which who knows it might
# Although I don't know why I am writing this here in the Inventory class becuase this probably wont be edited too often
# And I would be more likely to be reminded of it of I put it in the main class, or a class that I look at often like the
# Training class or something. But eh too late now..
class Inventory:

    def __init__(self):
        self.inventory = []
        for i in range(25):
            self.inventory.append('sword')

        self.file_path = 'data/data.json'
        self.save()

    # Maybe: Encrypt data so user can't easily edit their items
    def save(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        data['global_inventory'] = {}
        data['global_inventory']['value'] = self.inventory

        with open(self.file_path, 'w') as f:
            json.dump(data, f)

        print('Global Inventory Saved')
        print(self.inventory)

    def load(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        # Load variables
        self.inventory = data['global_inventory']['value']

        print('Global Inventory loaded')
        print(self.inventory)
