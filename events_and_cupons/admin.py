from user import User
from db import USERS

class Admin(User):
    def __init__(self, id, username, password, email, superuser):
        super().__init__(id, username, password, email)
        self.superuser = superuser

    def __repr__(self):
        return f'Admin_id: {self.id}, \n Admin_name: {self.username}, \n Admin_email: {self.email}, \n Superuser: {self.superuser}'

    @classmethod
    def create_user(cls, username, password, email):
        new_user = User(
            id = len(USERS) + 1,
            username = username,
            password = password,
            email = email
        )
        new_user.add()
        return new_user

    @classmethod
    def create_admin(cls, username, password, email):
        new_admin = Admin(
            id = len(USERS) + 1,
            username = username,
            password = password,
            email = email,
            superuser = True
        )
        return new_admin.add()

    @classmethod
    def update_user(cls, id, username, password, email):
        update_user = User.get_user_by_id(id)
        if update_user is None:
            return 'Usuario não encontrado'
        if isinstance(update_user, Admin):
            USERS[id-1] = Admin(id, username, password, email, superuser = True)
        else:
            USERS[id-1] = User(id, username, password, email)
        return USERS[id-1]

    @classmethod
    def get_user_by_id(cls, id):
        for user in USERS:
            if user.id == id:
                return user
        return None
    
    @classmethod
    def get_all_users(cls):
        return USERS

    @classmethod
    def delete_user(cls, id):
        user = cls.get_user_by_id(id)
        if user:
            USERS.remove(user)
            return user
        return "Usuario não encontrado"

    

        