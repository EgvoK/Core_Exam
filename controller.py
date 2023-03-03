import os
import sys

import config
import view
from model import Model
from view import *


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Controller:
    OPTIONS = {
        '1': 'Show all costs',
        '2': 'Add new cost',
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

    @staticmethod
    def show_report_menu():
        MenuDisplay.display(config.reports)

    def menu(self):
        cls()
        self.show_menu()

        while True:
            option = input("\nEnter the option number: ")
            cls()
            self.show_menu()
            if option in self.OPTIONS.keys():
                if option == "1":
                    view.ExpendituresDisplay.display()
                    self.model.get_expenditures()
                    self.show_menu()

                if option == "2":
                    self.model.add_expenditure()
                    view.ExpenditureAddDisplay.display()
                    self.show_menu()

                if option == "3":
                    self.show_report_menu()
                    while True:
                        report_option = input("\nEnter the option number: ")
                        if report_option in config.reports.keys():

                            if report_option == "1":
                                self.model.get_group_by_date()
                                self.show_report_menu()

                            if report_option == "2":
                                self.model.get_group_by_name()
                                self.show_report_menu()

                            if report_option == "3":
                                self.model.get_group_by_category()
                                self.show_report_menu()

                            if report_option == "4":
                                self.model.get_max_in_categories()
                                self.show_report_menu()

                            if report_option == "5":
                                pass

                            if report_option == "6":
                                self.model.get_min_in_categories()
                                self.show_report_menu()

                            if report_option == "7":
                                pass
                            if report_option == "8":
                                pass
                            if report_option == "0":
                                self.show_menu()
                                break
                        else:
                            print("Error! Incorrect option number!")

                if option == "4":
                    pass

                if option == "5":
                    pass

                if option == "6":
                    pass

                if option == "0":
                    print("Exit...")
                    sys.exit()

            else:
                print("Error! Incorrect option number!")


