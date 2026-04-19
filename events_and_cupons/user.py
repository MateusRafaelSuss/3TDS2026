from db import USERS, EVENTS, CUPONS
from event import Events
from cupon import Cupons
from datetime import datetime

class User():
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User_id: {self.id}, \n User_name: {self.username}, \n User_email: {self.email}, \n User_password: {self.password}'

    @classmethod
    def get_all_users(cls):
        return USERS

    def add(self):
        for user in USERS:
            if user.email == self.email and user.id != self.id:
                return f'Email já cadastrado'
        USERS.append(self)
        return self

    @classmethod
    def get_user_by_id(cls, id):
        for user in USERS:
            if user.id == id:
                return user
        return None

    def update_username(self, username):
        user = User.get_user_by_id(self.id)
        if user:
            user.username = username
            return user
        return 'Usuario não encontrado'

    def update_password(self, password):
        user = User.get_user_by_id(self.id)
        if user:
            user.password = password
            return user
        return 'Usuario não encontrado'

    def update_email(self, email):
        for users in USERS:
            if users.email == email and users.id != self.id:
                return 'Email já cadastrado'
        user = User.get_user_by_id(self.id)
        if user: 
            user.email = email
            return user
        return 'Usuario não encontrado'



    def create_events(self, title, description, date, local, base_price = 0):
        new_event = Events(
            id = len(EVENTS) + 1,
            title = title,
            description = description,
            date = date,
            local = local,
            user_id = self.id,
            base_price = base_price
        )
        new_event.add()
        return new_event

    def get_event_by_id(self, id):
        for events in EVENTS:
            if events.id == id:
                return events
        return None 

    def get_all_events(self):
        return EVENTS

    def get_events_by_user(self, user_id = None):
        if user_id == None:
            user_id = self.id
        return [event for event in EVENTS if event.user_id == user_id]


    def update_event_title(self, id, title):
        event = self.get_event_by_id(id)
        if event and event.user_id == self.id:
            event.title = title
            return event
        return 'Evento não encontrado'

    def update_event_description(self, id, description):
        event = self.get_event_by_id(id)
        if event and event.user_id == self.id:
            event.description = description
            return event
        return 'Evento não encontrado'

    def update_event_date(self, id, date):
        event = self.get_event_by_id(id)
        if event and event.user_id == self.id:
            event.date = date
            return event
        return 'Evento não encontrado'

    def update_event_local(self, id, local):
        event = self.get_event_by_id(id)
        if event and event.user_id == self.id:
            event.local = local
            return event
        return 'Evento não encontrado'

    def update_event_base_price(self, id, base_price):
        event = self.get_event_by_id(id)
        if event and event.user_id == self.id:
            event.base_price = base_price
            return event
        return 'Evento não encontrado'

    def delete_event(self, id):
        event = self.get_event_by_id(id)
        if event and event.user_id == self.id:
            EVENTS.remove(event)
            cupons_to_remove = [cupon for cupon in CUPONS if cupon.event_id == id]
            for cupon in cupons_to_remove:
                CUPONS.remove(cupon)
            return event
        return 'evento não encontrado'
            
    def create_cupon(self, title, expiration_date, discount_value, event_id):
        event = self.get_event_by_id(event_id)
        if not event:
            return 'Evento não encontrado'
        if event.user_id != self.id:
            return 'Você não tem permissão para criar um cupon neste evento'
        new_cupon = Cupons(
            id = len(CUPONS) + 1,
            title = title,
            expiration_date = expiration_date,
            discount_value = discount_value,
            event_id = event_id
        )
        new_cupon.add()
        return new_cupon

    def get_cupon_by_id(self, id):
        for cupon in CUPONS:
            if cupon.id == id:
                return cupon
        return None
    
    def get_all_cupons(self):
        return CUPONS

    def get_cupon_by_event(self, event_id):
        return [cupon for cupon in CUPONS if cupon.event_id == event_id]

    def update_cupon_title(self, id, title):
        cupon = self.get_cupon_by_id(id)
        if cupon:
            event = self.get_event_by_id(cupon.event_id)
            if event and event.user_id == self.id:
                cupon.title = title
                return cupon
            return 'Cupon não encontrado'

    def update_cupon_expiration_date(self, id, expiration_date):
        cupon = self.get_cupon_by_id(id)
        if cupon:
            event = self.get_event_by_id(cupon.event_id)
            if event and event.user_id == self.id:
                cupon.expiration_date = expiration_date
                return cupon
            return 'Cupon não encontrado'

    def update_cupon_discount_value(self, id, discount_value):
        cupon = self.get_cupon_by_id(id)
        if cupon:
            event = self.get_event_by_id(cupon.event_id)
            if event and event.user_id == self.id:
                cupon.discount_value = discount_value
                return cupon
            return 'Cupon não encontrado'

    def delete_cupon(self, id):
        cupon = self.get_cupon_by_id(id)
        if cupon:
            event = self.get_event_by_id(cupon.event_id)
            if event and event.user_id == self.id:
                CUPONS.remove(cupon)
                return cupon
            return 'Cupon não encontrado'

    def get_valid_cupons_by_event(self, event_id):
        valid_cupons = []
        day = datetime.now().date()
        for cupon in CUPONS:
            if cupon.event_id == event_id:
                expiration = datetime.strptime(cupon.expiration_date,"%Y-%m-%d").date()
                if expiration >= day:
                    valid_cupons.append(cupon)
        return valid_cupons

    def final_price(self, event_id):
        event = self.get_event_by_id(event_id)
        if not event:
            return 'Evento não encontrado'
        valid_cupons = self.get_valid_cupons_by_event(event_id)
        total_discount = sum(cupon.discount_value for cupon in valid_cupons)
        final_price = event.base_price - total_discount
        if final_price < 0:
            final_price = 0 
        return final_price


