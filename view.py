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







