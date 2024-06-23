import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Select database
db = client['mydatabase']

# Select collection
collection = db['mycollection']

      
# Sample search query
query = {
    "class_id": 24,
    "scores": {
        "$elemMatch": {
            "type": "exam",
            "score": {"$gt": 4}
        }
    }
}

# Execute the search query
results = collection.find(query)

# Print the results
for result in results:
    print(result)