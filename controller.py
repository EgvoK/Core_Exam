import os


from model import Model


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

    def menu(self):
        cls()
        pass
