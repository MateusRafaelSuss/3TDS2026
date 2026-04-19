from db import EVENTS

class Events():
    def __init__(self, id, title, description,  date, local, user_id, base_price = 0):
        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.local = local
        self.user_id = user_id
        self.base_price = base_price

    def __repr__(self):
        return f'Event_ID: {self.id}, \n Even_Title: {self.title},\, Event_description: {self.description}, \n Event_Date: {self.date}, \n Event_Local: {self.local}, Event_User_ID: {self.user_id}, Event_Base_Price: {self.base_price}'

    def add(self):
        EVENTS.append(self)