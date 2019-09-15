from pony.orm import Database, PrimaryKey, Required, Set, db_session, Optional
from uuid import uuid4 as gid, UUID
import datetime as dt



db = Database()



db.bind(provider='sqlite', filename='baza.sqlite', create_db=True)


class Profesor(db.Entity):
    id= PrimaryKey(str)
    Ime = Required(str)
    Prezime = Required(str)
    titula = Required(str)
    prosjecnaocjena = Optional(float)
    ankete=Set("Anketa")
    kolegiji=Set("Kolegij")

class Kolegij(db.Entity):
    id = PrimaryKey(str)
    naziv= Required(str)
    lozinka= Required(str)
    profesori = Set(Profesor)
    ankete=Set("Anketa")

class Anketa(db.Entity):
    id = PrimaryKey(str)
    profesori= Required(Profesor)
    kolegiji = Required(Kolegij)



db.generate_mapping(check_tables=True, create_tables=True)
