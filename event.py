from datetime import datetime
from decimal import Decimal
from typing import List, Dict
from user import User
from coupon import Coupon

class Event:
    def __init__(self, title: str, description: str, price: Decimal, date: datetime, location: str, users: List[User], regras: Dict):
        self.title = title
        self.description = description  
        self.price = price
        self.date = date
        self.location = location 
        self.users = users if users is not None else []  
        self.regras = regras
        self.coupons: List[Coupon] = []  
        
    def __repr__(self):
        return f'{self.title}, {self.description}, {self.price}, {self.date}, {self.location}, {self.users}, {self.coupons}'
    
    @classmethod
    def create_event(cls, data: Dict):
        return cls(
            title=data['title'],
            description=data['description'],
            price=data['price'],
            date=data['date'],
            location=data['location'],
            users=[],
            regras=data['regras']
        )
    
    def add_user(self, user: User):
        self.users.append(user)
        
    def add_users(self, users: List[User]):
        for user in users:
            self.users.append(user) 
        
    def apply_discount(self, coupon: Coupon):
        new_price = self.price - (self.price * coupon.discount)
        self.price = new_price
        
    def add_coupon(self, coupon: Coupon):
        self.coupons.append(coupon)  
        
    def add_coupons(self, coupons: List[Coupon]):
        for coupon in coupons:
            self.coupons.append(coupon)
