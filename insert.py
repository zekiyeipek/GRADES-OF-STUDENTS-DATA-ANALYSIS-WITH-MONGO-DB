import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Select database
db = client['mydatabase']

# Select collection
collection = db['mycollection']

# Open the file and read the JSON data
with open('grades.json') as f:
    # Load each JSON object separately and insert it into MongoDB
    for line in f:
        data = json.loads(line)
        
        # Remove the _id field if present
        if '_id' in data:
            del data['_id']
        
        result = collection.insert_one(data)
        print("Inserted document ID:", result.inserted_id)
        
        
# Sample search query
query = {"scores.type": "quiz", "scores.score": {"$gt": 20}}

# Execute the search query
results = collection.find(query)

# Print the results
for result in results:
    print(result)