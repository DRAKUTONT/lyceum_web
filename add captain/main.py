from os import environ

from flask import Flask

from data.db_session import db_init, create_session
from queries import add_user

app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret key'

if __name__ == "__main__":
    db_init('db/database.db')
    session = create_session()

    captain = {'surname': 'Scott',
               'name': 'Ridley',
               'age': 21,
               'position': 'captain',
               'speciality': 'research engineer',
               'address': 'module_1',
               'email': 'scott_chief@mars.org'}

    user_2 = {'surname': 'A',
              'name': 'A',
              'age': 21,
              'position': 'A',
              'speciality': 'A',
              'address': 'A',
              'email': 'A@mars.org'}

    user_3 = {'surname': 'B',
              'name': 'B',
              'age': 21,
              'position': 'B',
              'speciality': 'B',
              'address': 'B',
              'email': 'B@mars.org'}

    user_4 = {'surname': 'C',
              'name': 'C',
              'age': 21,
              'position': 'C',
              'speciality': 'C',
              'address': 'C',
              'email': 'C@mars.org'}

    add_user(session=session, data=captain)
    add_user(session=session, data=user_2)
    add_user(session=session, data=user_3)
    add_user(session=session, data=user_4)
