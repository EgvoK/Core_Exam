import config


class MenuDisplay:
    @staticmethod
    def display(option):
        print(f"{config.SEPARATOR}\nCOST ACCOUNTING APPLICATION\n{config.SEPARATOR}"
              f"\nThe following commands are available: ")
        for key, value in option.items():
            print(f"{key}. {value}")


class ExpendituresDisplay:
    @staticmethod
    def display():
        print(f"{config.SEPARATOR}\nLIST OF COST\n{config.SEPARATOR}")
        print("#. Name - Date - Category")


class ExpenditureAddDisplay:
    @staticmethod
    def display():
        print(f"{config.SEPARATOR}\nNew cost has been added!")


class ExportToCSV:
    @staticmethod
    def display():
        print(f"{config.SEPARATOR}\nExport to CSV-file is completed!")


class ImportFromCSV:
    @staticmethod
    def display():
        print(f"{config.SEPARATOR}\nImport from CSV-file is completed!")


class AddCategory:
    @staticmethod
    def display():
        print(f"{config.SEPARATOR}\nCategory is successfully added!")


class DelCategory:
    @staticmethod
    def display():
        print(f"{config.SEPARATOR}\nCategory has been deleted!")





