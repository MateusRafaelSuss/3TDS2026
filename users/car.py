from db import CARS

class Car:
    def __init__(self, id, brand, model, year, type_car):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.type_car = type_car
    
    def __repr__(self):
        return f"""Car_id: {self.id}, \n Car_brand: {self.brand}, \n Car_model: {self.model}, \n Car_year: {self.year}, \n Car_Type: {self.type_car}"""

    def add(self):
        CARS.append(self)

    