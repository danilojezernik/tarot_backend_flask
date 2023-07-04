import datetime
from dataclasses import asdict

from pymongo import MongoClient

from src import env
from src.domain.admin import Admin
from src.domain.objava import Objava

client = MongoClient(env.DB_CONNECTION)
proces = client[env.DB_PROCES]

objava = [
    asdict(Objava(naslov='Tarot 1',
                  podnaslov='Tarot karte 1',
                  vsebina='Morbi aliquam rutrum cursus. Donec id nisl id turpis rutrum condimentum ac et elit. Maecenas semper, magna non fermentum euismod, orci orci vulputate ligula, a hendrerit ex velit eget nibh. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed eu purus scelerisque, porta quam eget, rutrum arcu. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eros eros, tristique et tristique vitae, pretium at est. Cras efficitur est a magna interdum suscipit. Sed blandit finibus eleifend. Pellentesque nunc est, dictum ac dolor vel, lobortis consectetur libero. Nullam quis risus volutpat, posuere felis in, placerat tellus. Vestibulum odio turpis, commodo ac neque eu, commodo vulputate tortor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur purus nulla, imperdiet id imperdiet in, sodales eu turpis.',
                  slika='slika',
                  objavljeno=datetime.datetime.now())),
    asdict(Objava(naslov='Tarot 2',
                  podnaslov='Tarot karte 2',
                  vsebina='Morbi aliquam rutrum cursus. Donec id nisl id turpis rutrum condimentum ac et elit. Maecenas semper, magna non fermentum euismod, orci orci vulputate ligula, a hendrerit ex velit eget nibh. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed eu purus scelerisque, porta quam eget, rutrum arcu. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eros eros, tristique et tristique vitae, pretium at est. Cras efficitur est a magna interdum suscipit. Sed blandit finibus eleifend. Pellentesque nunc est, dictum ac dolor vel, lobortis consectetur libero. Nullam quis risus volutpat, posuere felis in, placerat tellus. Vestibulum odio turpis, commodo ac neque eu, commodo vulputate tortor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur purus nulla, imperdiet id imperdiet in, sodales eu turpis.',
                  slika='slika',
                  objavljeno=datetime.datetime.now())),
    asdict(Objava(naslov='Tarot 3',
                  podnaslov='Tarot karte 3',
                  vsebina='Morbi aliquam rutrum cursus. Donec id nisl id turpis rutrum condimentum ac et elit. Maecenas semper, magna non fermentum euismod, orci orci vulputate ligula, a hendrerit ex velit eget nibh. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed eu purus scelerisque, porta quam eget, rutrum arcu. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eros eros, tristique et tristique vitae, pretium at est. Cras efficitur est a magna interdum suscipit. Sed blandit finibus eleifend. Pellentesque nunc est, dictum ac dolor vel, lobortis consectetur libero. Nullam quis risus volutpat, posuere felis in, placerat tellus. Vestibulum odio turpis, commodo ac neque eu, commodo vulputate tortor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur purus nulla, imperdiet id imperdiet in, sodales eu turpis.',
                  slika='slika',
                  objavljeno=datetime.datetime.now())),
    asdict(Objava(naslov='Tarot 4',
                  podnaslov='Tarot karte 4',
                  vsebina='Morbi aliquam rutrum cursus. Donec id nisl id turpis rutrum condimentum ac et elit. Maecenas semper, magna non fermentum euismod, orci orci vulputate ligula, a hendrerit ex velit eget nibh. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed eu purus scelerisque, porta quam eget, rutrum arcu. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eros eros, tristique et tristique vitae, pretium at est. Cras efficitur est a magna interdum suscipit. Sed blandit finibus eleifend. Pellentesque nunc est, dictum ac dolor vel, lobortis consectetur libero. Nullam quis risus volutpat, posuere felis in, placerat tellus. Vestibulum odio turpis, commodo ac neque eu, commodo vulputate tortor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur purus nulla, imperdiet id imperdiet in, sodales eu turpis.',
                  slika='slika',
                  objavljeno=datetime.datetime.now())),
]

login = [
    asdict(Admin(uporabnisko_ime=env.UPORABNIK, geslo=env.GESLO))
]


def drop():
    proces.objava.drop()


def seed():
    proces.objava.insert_many(objava)

