from pymongo.mongo_client import MongoClient
import bson.json_util as json_util
import json
import os

def getLastDate(carID):
    #Conexión a MongoDB para encontrar el registro más reciente con la matrícula de ese coche
    client = MongoClient(os.getenv("URL"))
    database = client.get_database(os.getenv("DATABASE"))
    collection = database.get_collection(os.getenv("COLLECTION"))
    result = collection.find_one({"car_id": carID})
    data = json_util.dumps(result)
    content = json.loads(data)

    return content


