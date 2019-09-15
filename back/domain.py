from model import  Profesor,Anketa,Kolegij
from pony.orm import db_session, select
from uuid import uuid4 as gid, UUID

class Kolegiji:
    @db_session()
    def listaj():
        # ORM upit
        q = select(s for s in Kolegij)
        def dohvati_veze_profesora(x):
            if "profesori" in x:
                x["profesori"] = [Profesor[z].to_dict() for z in x ["profesori"]]
            return x
        kolegiji=[dohvati_veze_profesora(s.to_dict(with_collections=True)) for s in q]
        return kolegiji

    
    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            if "profesori" in s:
                profesori_kolegija = s["profesori"]
                svi_profesori = list(Profesor[x] for x in profesori_kolegija)
                s["profesori"] = svi_profesori
            kreiran_kolegij = Kolegij(**s)
            return True,  kreiran_kolegij.id
        except Exception as e:
            return False, str(e)
    
class Ankete:
    @db_session()
    def listaj():
       
        q = select(s for s in Anketa)
        data = [x.to_dict() for x in q]
        return data,


    @db_session()
    def dodaj(s):
        try:
            s["id"] = str(gid())
            s = Anketa(**s)
            return True, None
        except Exception as e:
            return False, str(e)

    
class Profesori:
    @db_session()
    def listaj():
        q = select(s for s in Profesor)
        data = [x.to_dict() for x in q]
        return data,

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            novi = Profesor(**s)
            return True, novi.id
        except Exception as e:
            return False, str(e)


    @db_session
    def update(s):
        try:
            s = Profesor[s["id"]].set(**s)
            return True, None
        except Exception as e:
            return False, str(e)