import pymongo
import datetime
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.aovtsinn
db.aovtsinn.count()
aovtsinn = db.aovtsinn
aovtsinn.find()

print ("Homework \"Mongo\" created by Artur Ovtsinnikov")
 

for k in range(2000):
    aovtsinn = db.clients.insert({"birthdate":"1975-01-01"});
print (k)
print ("Generated 2000 records with birthdate 1975")

for l in range(4000):
    aovtsinn = db.clients.insert({"birthdate":"1985-01-01"});
print (l)
print ("Generated 4000 records with birthdate 1985")

for m in range(2000):
    aovtsinn = db.clients.insert({"birthdate":"1995-01-01"});
print (m)
print ("Generated 2000 records with birthdate 1995")

for i in range(100):
   aovtsinn = db.clients.insert({"name":"Tom"});
print (i)
print ("Generated 100 records with name Tom")

for j in range(100):
   aovtsinn = db.clients.insert({"name":"Tomas"});
print (j)
print("Generated 100 records with name Tomas")

for b in range(1800):
   aovtsinn = db.clients.insert({"name":"Arthur"});
print (b)
print ("Generated 1800 records with my name Arthur")

print ("\n")
print ("The Total Amount of clients is")
print (db.clients.count())

print ("\n")
print ("The birthday is less than (before) \"1990-01-01\" is")
print ( db.clients.find({"birthdate":{"$lt":"1990-01-01"}}).count())

print ("\n")
print ("The birthday is greater than (after) \"1980-01-01\" is")
print (db.clients.find({"birthdate":{"$gt":"1980-01-01"}}).count())

print ("\n")
print ("The amount of records where \"name\" is \"Tom\" is")
print (db.clients.find({"name":"Tom"}).count())

print ("\n")
print ("The amount of records where \"name\" starts with \"Tom\" is")
print (db.clients.find({"name":{"$regex":"^Tom"}}).count())

print ("\n")

