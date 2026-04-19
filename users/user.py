from db import USERS
from db import CARS
from car import Car
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"{self.id}, \n {self.username}, \n {self.email} \n {self.password})"

    @classmethod
    def get_all_users(cls):
        return USERS

    def add(self):
        USERS.append(self)
    
    def update_username(self, username):
        user = User.get_user_by_id(self.id)
        if user:
            user.username = username
            return user
        return 'Usuário não encontrado'
    
    def update_password(self, password):
        user = User.get_user_by_id(self.id)
        if user:
            user.password = password
            return user
        return 'Usuário não encontrado'
    
    def update_email(self, email):
        user = User.get_user_by_id(self.id)
        if user:
            user.email = email
            return user
        return 'Usuário não encontrado'


    def get_car_by_id(self, id):
        for car in CARS:
            if car.id == id:
                return car
            return None

    def create_car(self, brand, model, year, type_car):
        new_car = Car(
            id = len(CARS) + 1,
            brand = brand,
            model = model,
            year = year,
            type_car = type_car,
        )
        new_car.add()
        return new_car
    
    def get_all_cars(self):
        return CARS
    
    def update_car_brand(self, id, brand):
        car = self.get_car_by_id(id)
        if car: 
            car.brand = brand
            return car
        return 'Carro não encontrado'


    def update_car_model(self, id, model):
        car = self.get_car_by_id(id)
        if car:
            car.model = model
            return car
        return 'Carro não encontrado'

    def update_car_year(self, id, year):
        car = self.get_car_by_id(id)
        if car:
            car.year = year
            return car
        return 'Carro não encontrado'

    def update_car_type(self, id, type_car):
        car = self.get_car_by_id(id)
        if car:
            car.type_car = type_car
            return car
        return 'Carro não encontrado'

    def delete_car(self, id):
        car = self.get_car_by_id
        if car:
            CARS.remove(car)
            return car
        return 'Carro não encontrado'