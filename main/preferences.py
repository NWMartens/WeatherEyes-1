"""import pymongo
from pymongo import MongoClient

class StorePreferencesPost:
    def __init__ (self, dictionary):
        self.dictionary = dictionary
        self.temp = self.dictionary['TempUnit']
        self.timeframe = self.dictionary['HRorDAY']
        self.provider = self.dictionary['ServiceProvider']
        self.munit = self.dictionary['Munit']
        self.datatype = self.dictionary['datatype']
        user.username 
    pass


class Preferences:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://team:team@cluster0.yknbr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.preferences = self.pullFromMongo()
        for dictionary in self.preferences:
            if dictionary.key == 'datatype':
                self.datatype = dictionary['datatype']
            elif dictionary.key == 'ServiceProvider':
                self.ServiceProvider = dictionary['ServiceProvider']
            elif dictionary.key == 'HRorDAY':
                self.HRorDLY = dictionary['HRorDAY']
            elif dictionary.key == 'Munit':
                self.MUnit = dictionary['Munit']
            elif dictionary.key == 'TempUnit':
                self.TempUnit = dictionary['TempUnit']

    def pullFromMongo(self):
        db = self.client ["user"]
        collection = db['auth_user']
        preferences = collection.find
        #find based on user name
        preferences = collection.find
        #return a list of dictionaries
        #[{'datatype': },{'ServiceProvider;}, {'HRorDLY': },{'MUnit': }, {'TempUnit': }]

    def Temp(self):
        TempUnit = self.TempUnit
        if TempUnit == 'Kelvin':
            return "Temp(K)"
        elif TempUnit == 'Celsius':
            return "Temp(C)"
        elif TempUnit == 'Farenheit':
            return "Temp(F)"

    def MinTemp(self):
        TempUnit = self.TempUnit
        if TempUnit == 'Kelvin':
            return "MinTemp(K)"
        elif TempUnit == 'Celsius':
            return "MinTemp(C)"
        elif TempUnit == 'Farenheit':
            return "MinTemp(F)"

    def MaxTemp(self):
        TempUnit = self.TempUnit
        if TempUnit == 'Kelvin':
            return "MaxTemp(K)"
        elif TempUnit == 'Celsius':
            return "MaxTemp(C)"
        elif TempUnit == 'Farenheit':
            return "MaxTemp(F)"

    def Munit (self):
        munit = self.MUnit
        if munit == 'Millimeters':
            return 'Precipitation_m'
        elif munit == 'Inches':
            return 'Precipitation_i'
"""