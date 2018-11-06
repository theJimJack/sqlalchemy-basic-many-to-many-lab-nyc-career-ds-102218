#updated from import to seed from models
from seed import *
# Session = sessionmaker()
# session = Session.configure(bind = engine)

def return_christian_bales_roles():
    return session.query(Role.character).join(Actor_Role).join(Actor).filter(Actor.name == "Christian Bale").all()
    # Return a list of Christian Bale role instances

def return_catwoman_actors():
    return session.query(Actor.name).join(Actor_Role).join(Role).filter(Role.character == "Catwoman").all()
    #  Return a list of actor instances that have played Catwoman

def return_number_of_batman_actors():
    return len(session.query(Actor.name).join(Actor_Role).join(Role).filter(Role.character == "Batman").all())
    # Return the number of actors that have played Batman
