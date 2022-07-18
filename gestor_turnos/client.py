

class Client:

    def __init__(self, name, surname, dni):
        self.name = name
        self.surname = surname
        self.__dni = dni

    def __str__(self):
        return f"{self.name} {self.surname}"

    def get_dni(self):
        return self.__dni

    def set_dni(self, number):
        self.__dni = number
