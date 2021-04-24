#don't forget to pip install dnsdpython
"""
{% load static %}
<img src = {% static 'main/image/weatherEyes.png%}>
"""
import pymongo
from pymongo import MongoClient

class StorePreferencesPost():
    def __init__ (self, dictionary, user):
      self.user = user
      self.dictionary = dictionary
      self.temp = self.dictionary['TempUnit']
      self.timeframe = self.dictionary['HRorDAY']
      self.provider = self.dictionary['ServiceProvider']
      self.munit = self.dictionary['Munits']
      self.datatype = self.dictionary['datatype']
      self.storemongo()
    """
    def storemongo(self):
      client = pymongo.MongoClient("mongodb+srv://team:team@cluster0.yknbr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
      db = client["User"]
      collection = db['Preference']
      preferences = {'username':self.user, 'datatype':self.datatype,'ServiceProvider':self.provider,'HRorDAY':self.timeframe,'Munit': self.munit,'TempUnit':self.temp}
      new_data = preferences
      post_id = collection.insert_one(new_data).inserted_id

    """
    def storemongo(self):
      client = pymongo.MongoClient("mongodb+srv://team:team@cluster0.yknbr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
      db = client["User"]
      collection = db['Preference']
      collection.find_and_modify(query={'username': self.user}, update ={'username':self.user,'datatype':self.datatype,'ServiceProvider':self.provider,'HRorDAY':self.timeframe,'Munit': self.munit,'TempUnit':self.temp})

"""
class Preferences:
    def __init__(self, username):
        self.username = username
        self.preferences = []
        self.pullFromMongo()
        for x in self.preferences:
            self.datatype = x['datatype'] 
            self.serviceprovider = x['ServiceProvider'] 
            self.HRorDAY = x['HRorDAY'] 
            self.TempUnit = x['TempUnit'] 
            self.MUnit = x['Munit']
        
    def pullFromMongo(self):
        client = pymongo.MongoClient("mongodb+srv://team:team@cluster0.yknbr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client['User']
        collection = db['Preference']
        self.preferences = collection.find({'username':self.username})
        #return a list of dictionaries
        #[{'datatype': },{'ServiceProvider;}, {'HRorDLY': },{'MUnit': }, {'TempUnit': }]

    def Temp(self):
        TempUnit = self.TempUnit
        if TempUnit == 'Kelvin':
            return "TemperatureK"
        elif TempUnit == 'Celsius':
            return "TemperatureC"
        elif TempUnit == 'Farenheit':
            return "TemperatureF"

    def MinTemp(self):
        TempUnit = self.TempUnit
        if TempUnit == 'Kelvin':
            return "MinTempK"
        elif TempUnit == 'Celsius':
            return "MinTempC"
        elif TempUnit == 'Farenheit':
            return "MinTempF"

    def MaxTemp(self):
        TempUnit = self.TempUnit
        if TempUnit == 'Kelvin':
            return "MaxTempK"
        elif TempUnit == 'Celsius':
            return "MaxTempC"
        elif TempUnit == 'Farenheit':
            return "MaxTempF"

    def Munit (self):
        munit = self.MUnit
        if munit == 'Millimeters':
            return 'Precipitation_m'
        elif munit == 'Inches':
            return 'Precipitation_i'
"""