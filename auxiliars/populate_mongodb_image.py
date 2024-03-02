from pymongo import MongoClient
from datetime import datetime
import os

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Create or select a database
db = client.get_database('car_locations')

# Create or select a collection
collection = db.get_collection('car_last_date')


with open('../caso5_results.txt', 'r') as file:
    for line in file:
        row = line.strip().split(' ')
        id = row[0]
        last_date = row[1][1:] + ' ' + row[2][:-1]
        collection.insert_one({
            'car_id': row[0],
            'last_date': datetime.strptime(last_date, "%d/%m/%Y %H:%M:%S")
        })




