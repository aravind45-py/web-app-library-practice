import pymongo
import pprint
client = pymongo.MongoClient("mongodb+srv://aravind:aravind@cluster1.lkblz.mongodb.net/new?retryWrites=true&w=majority")
db = client.get_database('beta')
col = db.get_collection('test')

for i in col.find():
    pprint.pprint(i)
# col.insert_one({'_id':2,"name":"kasi"})
# for i in col.find():
#     pprint.pprint(i)
col.update_one({'author':'a'},{"$set":{'rating':32}})
for i in col.find():
    pprint.pprint(i)