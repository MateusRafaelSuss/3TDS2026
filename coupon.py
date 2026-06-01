from datetime import datetime
from decimal import Decimal
from typing import Dict

class Coupon:
    def __init__(self, title: str, expires_at: datetime, discount: Decimal):
        self.title = title
        self.expires_at = expires_at
        self.discount = discount
        
    def __repr__(self):
        return f'{self.title}, {self.expires_at}, {self.discount}'
    
    @classmethod
    def create_coupon(cls, data: Dict):  
        return cls(
            title=data['title'],
            expires_at=data['expires_at'],
            discount=data['discount']
        )
