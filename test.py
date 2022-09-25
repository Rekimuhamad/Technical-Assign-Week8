from sqlite3 import Timestamp
from flask import Flask,request
import pymongo
import datetime

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://Rext:<rekiakbar>@cluster0.ha5j7v8.mongodb.net/?retryWrites=true&w=majority")

db = client.reki
collection = db.smkn4

@app.route('/week8',methods=['GET','POST'])
def location_application():
    kecepatan= request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    save_to_db(kecepatan=kecepatan,latitude=latitude,longitude=longitude)
    return{
        "output":{
            "kecepatan":kecepatan,
            "latitude":latitude,
            "longitude":longitude,
            "timestamp": datetime.datetime.now()
        }
    }

if __name__ == '__main__':
    app.run(debug=True)