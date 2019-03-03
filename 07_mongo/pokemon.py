#HeartGold -- Karen Li, Thomas Lee
#SoftDev2 pd6
#K07 -- Import/Export Bank
#2019-03-02

import pymongo, json

SERVER_ADDR="142.93.206.119"
connection=pymongo.MongoClient(SERVER_ADDR)
connection.drop_database("HeartGold")
db = connection.HeartGold
collection = db.pokemon

f = open("pokedex.json")
data = json.load(f)
collection.insert_many(data["pokemon"])

def find_id(pokemon_id):
    return collection.find({"id": pokemon_id})

def find_name(name):
    return collection.find({"name": name})

def find_type(pokemon_type):
    return collection.find({"type": pokemon_type})

def find_weakness(weakness):
    return collection.find({"weaknesses": weakness})

def find_type_weakness(pokemon_type, weakness):
    return collection.find({"$and":[{"type": pokemon_type}, {"weaknesses": weakness}]}) 

print("=====POKEMON WITH ID 1=====")
display_pokemon(find_id(1))

print("=====POKEMON WITH NAME Jigglypuff=====")
display_pokemon(find_name("Jigglypuff"))

print("=====POKEMON WITH TYPE GRASS=====")
display_pokemon(find_type("Grass"))

print("=====POKEMON WITH WEAKNESS WATER=====")
display_pokemon(find_weakness("Water"))

print("=====POKEMON WITH TYPE DRAGON AND WEAKNESS DRAGON=====")
display_pokemon(find_type_weakness("Dragon", "Dragon"))
