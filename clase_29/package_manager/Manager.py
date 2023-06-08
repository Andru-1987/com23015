import json
import os
from uuid import uuid4


class Beer():
    def __init__(self,**kwargs):
        self.beer_id : str(uuid4()) 
        self.nombre : kwargs["nombre"],
        self.abv : kwargs["abv"],
        self.url : kwargs["url"]

    def __dict__(self):
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
     
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
path = "./db/beer_db.json"

file = os.path.join(BASE_DIR , "package_manager",path)

beer_manager = Manager(file)

print(beer_manager.db_reader())

beer_insert = Beer(
    
)


