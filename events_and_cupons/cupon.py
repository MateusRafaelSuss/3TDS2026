from db import CUPONS

class Cupons():
    def __init__(self, id, title, expiration_date, discount_value, event_id):
        self.id = id
        self.title = title
        self.expiration_date = expiration_date
        self.discount_value = discount_value
        self.event_id = event_id

    def __repr__(self):
        return f'Cupon_ID: {self.id}, \n Cupon_Title: {self.title}, \n Cupon_expiration_date: {self.expiration_date}, \n Cupon_Discount_value: {self.discount_value}, \n Cupon_event_id: {self.event_id}'

    def add(self):
        CUPONS.append(self)