import sys

from us_visa.exception import USVisaException
from us_visa.logger import logging
from urllib.parse import quote_plus

import os,pymongo,certifi
from us_visa.constants import DATABASE_NAME,MONGODB_USERNAME,MONGODB_PASSWORD

ca = certifi.where()

class MongoDBClient:
    """
    class Name : export data into feature store
    Description : This method exports the dataframe from mongodb feature store as dataframe

    Output : connection to mongodb database
    On Failure : raises an exception 
    """

    client = None

    def __init__(self,database_name=DATABASE_NAME)->None:
        try:
            if MongoDBClient.client is None:
                mongo_db_username = os.environ.get('MONGODB_USERNAME')
                mongo_db_password = os.environ.get('MONGODB_PASSWORD')

                if mongo_db_username and mongo_db_password:
                    escaped_username = quote_plus(mongo_db_username)
                    escaped_password = quote_plus(mongo_db_password)
                mongo_db_url = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.n8c403t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
                if mongo_db_url is None:
                    raise Exception(f"Either of mongodb username and password is not set")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info('MongoDB connection succesfull')
        except Exception as e:
            raise USVisaException(e,sys)

