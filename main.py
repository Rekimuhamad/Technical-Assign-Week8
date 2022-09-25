from cmath import rect
from logging import exception
import pymongo
from flask import Flask,request



client = pymongo.MongoClient("mongodb+srv://Rext:<rekiakbar>@cluster0.ha5j7v8.mongodb.net/?retryWrites=true&w=majority")

db = client.reki
collection =db.smkn4

def sans (kecepatan,latitude,longitude) -> tuple:
    try:
        data = {
            "kecepatan": kecepatan,
            "latitude": latitude,
            "logitude": longitude,
            
        }

        rec_idl = collection.insert_one(data)

        print("Data direcord",rec_idl)
        return True,None
    except Exception as e:
      return False,str(e)