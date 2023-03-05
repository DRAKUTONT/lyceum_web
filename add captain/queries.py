import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.users import User


def add_user(session: orm.Session, data: dict):
    user = User()
    user.surname = data['surname']
    user.name = data['name']
    user.age = data['age']
    user.position = data['position']
    user.speciality = data['speciality']
    user.address = data['address']
    user.email = data['email']

    session.add(user)
    session.commit()