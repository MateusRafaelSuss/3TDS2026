from car import Car
from user import User
from admin import Admin
from db import CARS

new_user = User(1, "Mateus", "123", "email@gmail.com")
new_car = new_user.create_car('Toyota', 'Corolla', 2012, 'sedan')
print(new_car)

update = new_user.update_car_model(1, 'Hilux')
update1 = new_user.update_car_type(1, 'pickup')
print(new_user.get_all_cars())