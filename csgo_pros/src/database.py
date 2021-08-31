import os
import csv

import pymongo
from dotenv import load_dotenv

load_dotenv()
if os.getenv('MONGO_URL') is None:
    try:
        url = open('db_url.txt', 'r').read().replace('\n', '')
    except FileNotFoundError as e:
        url = "localhost:27017"
    os.environ["MONGO_URL"] = url


def get_collection():
    client = pymongo.MongoClient(os.getenv('MONGO_URL'))
    db = client['csgo_pros']

    collection_name = 'players'
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)

    return db[collection_name]

def backup(filepath):
    if not filepath.endswith('.csv'):
        filepath = filepath + '.csv'

    client = pymongo.MongoClient(os.getenv('MONGO_URL'))
    data = client['csgo_pros']['players'].find()
    with open(filepath, 'w+') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'nickname', 'start_date', 'end_date', 'real_name', 'country', 'team', 'age',
                                                  'rating', 'dpr', 'kast', 'impact', 'adr', 'kpr',
                                                  'total_kills', 'headshot_percentage', 'total_deaths', 'kd'])
        writer.writeheader()
        for item in data:
            del item['_id']
            writer.writerow(item)


def restore(filepath):
    client = pymongo.MongoClient(os.getenv('MONGO_URL'))
    collection = client['csgo_pros']['players']
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["age"] = int(row["age"])
            row["rating"] = float(row["rating"])
            row["dpr"] = float(row["dpr"])
            row["kast"] = float(row["kast"])
            row["impact"] = float(row["impact"])
            row["adr"] = float(row["adr"])
            row["kpr"] = float(row["kpr"])
            row["total_kills"] = int(row["total_kills"])
            row["headshot_percentage"] = float(row["headshot_percentage"])
            row["total_deaths"] = int(row["total_deaths"])
            row["kd"] = float(row["kd"])
            collection.insert(row)


