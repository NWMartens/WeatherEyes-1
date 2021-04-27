import pymongo
from pymongo import MongoClient

class StoreRegistrationPost():
    def __init__ (self, dictionary):
      self.dictionary = dictionary
      self.user = self.dictionary['username']
      self.password = self.dictionary['password1']
      self.email = self.dictionary['email']
      self.storemongo()

    def storemongo(self):
      client = pymongo.MongoClient("mongodb+srv://team:team@cluster0.yknbr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
      db = client["User"]
      collection = db['Preference']
      userinfo = {'username':self.user, 'password':self.password,'email':self.email}
      new_data = userinfo
      post_id = collection.insert_one(new_data).inserted_id

   