import os

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


