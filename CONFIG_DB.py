import pymongo
import os

# Use environment variable for MongoDB connection, fallback to original
MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://debnathkuntal049:ZX0KCVyKHMM5yfGJ@cluster0.u9yav.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

client = pymongo.MongoClient(MONGO_URI)

result = str(client)

if "connect=True" in result:
    try:
        print("CONFIG DB CONNECTED SUCCESSFULLY ✅")
    except:
        pass
else:
    try:
        print("CONFIG DB CONNECTION FAILED ❌")
    except:
        pass

COLLECTIONS = client["CONFIG_DATABASE"]
BLACKLISTED_SKS = COLLECTIONS.BLACKLISTED_SKS
TOKEN_DB = COLLECTIONS.TOKEN_DB
SKS_DB = COLLECTIONS.SKS_DB
