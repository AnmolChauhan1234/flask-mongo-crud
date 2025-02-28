# import os
# from mongoengine import connect

# MONGO_URI = os.getenv("MONGODB_URI")
# # connect(db="user_database", host=MONGO_URI)
# connect(host=MONGO_URI)




import os
from mongoengine import connect
from dotenv import load_dotenv
load_dotenv()

# Default MongoDB URI

MONGO_URI = os.getenv("MONGODB_URI")

if not MONGO_URI:
    raise ValueError("Error: MONGODB_URI is not set in the .env file")

# Connect to MongoDB
try:
    
    connect(
        db="user_db",  
        host=MONGO_URI,
        alias="default"
    )
except Exception as e:
    print(e)
