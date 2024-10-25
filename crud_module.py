# John Miller
# CS - 340
# Module 4 Milestone

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):

        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        #If data is not empty
        if data is not None:
            #Try to insert data
            try:
                result = self.collection.insert_one(data)
                #Return boolean to indicate if insertion was successful
                return True if result.inserted_id else False
            except Exception as e:
                print(f"An error occurred during insertion: {e}")
                return False
        else:
                raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        #If query is not empty
        if query is not None:
            #Try to find the query
            try:
                #Return the query formatted as a list
                return list(self.collection.find(query))
            except Exception as e:
                #Catch any errors and return an empty list
                print(f"An error occurred during query: {e}")
                return []
        else:
            raise Exception("Nothing to read because query parameter is empty")

    def update(self, query, updateData, updateMany=False):
        if query and updateData is not None:
            if updateMany:
                result = self.collection.update_many(query, {"$set": updateData})
                return result.modified_count
            else:
                result = self.collection.update_one(query, {"$set": updateData})
                return result.modified_count
        else:
            raise Exception("Must have a query of documents to update and data to update.")

    def delete(self, query):
        if query is not None:
            result = self.collection.delete_many(query)
            return result.deleted_count


