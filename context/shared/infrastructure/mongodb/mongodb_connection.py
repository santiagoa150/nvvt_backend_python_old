from pymongo import MongoClient
from config import Settings

settings = Settings()


class MongoDBClient:

    def __init__(self):
        mongo_client = MongoClient(settings.mongodb_connection_uri)
        self.__database = mongo_client[settings.mongodb_database_name]

    def get_database(self):
        return self.__database
