import os


from model import Model
from view import *


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Controller:
    OPTIONS = {
        '1': 'Show all expenditures',
        '2': 'Add new expenditure',
        '3': 'Show reports',
        '4': 'Export to file',
        '5': 'Import from file',
        '6': "Categories settings",
        '0': 'Exit'
    }

    def __init__(self):
        self.model = Model()

    def show_menu(self):
        MenuDisplay.display(self.OPTIONS)

    def menu(self):
        cls()
        self.show_menu()

