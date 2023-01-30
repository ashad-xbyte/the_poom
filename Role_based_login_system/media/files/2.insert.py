import hashlib

import pymongo
import pandas as pd
import json


if __name__ == '__main__':
    print("Welcome to pymongo")
    #Connect To Mongo DB With Connection String

    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)

    db = client["Siraj"]
    collection = db["Edu_details"]
    # collection = db["Student_Details"]

    #insert Only One  document  Into Dictonary
    dictionary_one = {'STD':'SSC','Percentage':'68%'}
    collection.insert_one(dictionary_one)

    # insert Many document  Into Dictonary
    # dictionary_many = [
    #     {'name':'Krunal','marks':45,'Location':'Ahmedabad'},
    #     {'name':'XYZ','marks':50,'Location':'Surat'},
    #     {'name':'ABC','marks':150,'Location':'Kolkaat'},
    #     {'name':'asdf','marks':60,'Location':'Chennai'},
    #     {'name':'ghj','marks':90,'Location':'Delhi'}
    # ]
    # collection.insert_many(dictionary_many)
    # collection.update_many({},{'$set':{"Status" : "Pending"}})
