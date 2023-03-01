import config


class MenuDisplay:
    @staticmethod
    def display(option):
        print(f"{config.SEPARATOR}\nWELCOME TO COST ACCOUNTING\n{config.SEPARATOR}"
              f"\nThe following commands are available: ")
        for key, value in option.items():
            print(f"{key}. {value}")
        print("\n")


class ExpendituresDisplay:
    @staticmethod
    def display():
        print(f"{config.SEPARATOR}\nLIST OF COST\n{config.SEPARATOR}")
        print("#. Name - Date - Category")

