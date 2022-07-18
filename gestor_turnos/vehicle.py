
class Vehicle:
    def __init__(self, brand, model, plate):
        self.brand = brand
        self.model = model
        self.__plate = plate

    def __str__(self):
        return f"{self.brand} {self.model}. Patente {self.__plate}"

    def set_plate(self, new_plate):
        self.__plate = new_plate

    def get_plate(self):
        return self.__plate
