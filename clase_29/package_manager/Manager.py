import json
import os
from uuid import uuid4


class Beer():
    def __init__(self,**kwargs):
        id = uuid4()
        self.beer_id = str(id)
        self.nombre = kwargs["nombre"]
        self.abv = kwargs["abv"]
        self.url = kwargs["url"]

    def dict(self):
        return {
        "beer_id":self.beer_id,
        "nombre":self.nombre,
        "abv":self.abv,
        "url":self.url
        }


class Manager():
    def __init__(self,path):
        self.path = path
    
    def db_reader(self):
        with open(self.path, "r") as db:
            data = json.load(db)
            return data
    def db_create(self, beer:Beer):
        data = self.db_reader()
        data.append(beer)
        with open(self.path, "w") as db:
            json.dump(data,db,indent=4)

    def db_update(self,beer:Beer):
        pass
    
    def db_delete(self,beer:Beer):
        pass
        
    def db_search_one(self,beer_id:Beer):
        pass


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
path = "./db/beer_db.json"

file = os.path.join(BASE_DIR , "package_manager",path)

beer_manager = Manager(file)

print(beer_manager.db_reader())

beer_insert = Beer(
    nombre = "ginger ale",
    abv = 14 ,
    url = "https://www.acouplecooks.com/wp-content/uploads/2020/08/Ginger-Beer-001.jpg"
)


beer_manager.db_create(beer_insert.dict())

