import pymongo

# MongoDB connection string
mongodb_url = "mongodb://localhost:27017/"

# Connect to MongoDB
client = pymongo.MongoClient(mongodb_url)

# Access a specific database (replace 'mydatabase' with your database name)
database = client["mydatabase"]

# Optionally, authenticate if your MongoDB instance requires authentication
# database.authenticate(username, password)

# Print a success message
print("Connected to MongoDB")

from datetime import datetime

from datetime import datetime, timezone

blog_post = {
    "author": "John Doe",
    "title": "Introduction to MongoDB",
    "content": "MongoDB is a NoSQL database...",
    "tags": ["MongoDB", "NoSQL", "Database"],
    "created_at": datetime.now(timezone.utc),
    "comments": [
        {
            "author": "Alice",
            "text": "Great article!",
            "created_at": datetime.now(timezone.utc)
        },
        {
            "author": "Bob",
            "text": "Thanks for sharing!",
            "created_at": datetime.now(timezone.utc)
        }
    ]
}

print(blog_post)

from datetime import datetime, timezone
import pymongo

# MongoDB connection string
mongodb_url = "mongodb://localhost:27017/"

# Connect to MongoDB
client = pymongo.MongoClient(mongodb_url)

# Access a specific database (replace 'mydatabase' with your database name)
database = client["mydatabase"]

# Define sample documents for collections
blog_post = {
    "author": "John Doe",
    "title": "Introduction to MongoDB",
    "content": "MongoDB is a NoSQL database...",
    "tags": ["MongoDB", "NoSQL", "Database"],
    "created_at": datetime.now(timezone.utc),
    "comments": [
        {
            "author": "Alice",
            "text": "Great article!",
            "created_at": datetime.now(timezone.utc)
        },
        {
            "author": "Bob",
            "text": "Thanks for sharing!",
            "created_at": datetime.now(timezone.utc)
        }
    ]
}

user = {
    "username": "johndoe",
    "email": "johndoe@example.com",
    "created_at": datetime.now(timezone.utc)
}

# Insert documents into collections
blog_posts_collection = database["blog_posts"]
users_collection = database["users"]

blog_result = blog_posts_collection.insert_one(blog_post)
user_result = users_collection.insert_one(user)

# Print the IDs of the inserted documents
print("Inserted blog post ID:", blog_result.inserted_id)
print("Inserted user ID:", user_result.inserted_id)

from datetime import datetime, timezone
import pymongo

# MongoDB connection string
mongodb_url = "mongodb://localhost:27017/"

# Connect to MongoDB
client = pymongo.MongoClient(mongodb_url)

# Access a specific database (replace 'mydatabase' with your database name)
database = client["mydatabase"]

# Define sample data for insertion
user_data = {
    "username": "example_user",
    "email": "user@example.com",
    "created_at": datetime.now(timezone.utc)
}

post_data = {
    "author": "John Doe",
    "title": "Introduction to MongoDB",
    "content": "MongoDB is a NoSQL database...",
    "tags": ["MongoDB", "NoSQL", "Database"],
    "created_at": datetime.now(timezone.utc),
    "comments": [
        {
            "author": "Alice",
            "text": "Great article!",
            "created_at": datetime.now(timezone.utc)
        },
        {
            "author": "Bob",
            "text": "Thanks for sharing!",
            "created_at": datetime.now(timezone.utc)
        }
    ]
}

# Insert data into collections
users_collection = database["users"]
posts_collection = database["posts"]

user_result = users_collection.insert_one(user_data)
post_result = posts_collection.insert_one(post_data)

# Print the IDs of the inserted documents
print("Inserted user ID:", user_result.inserted_id)
print("Inserted post ID:", post_result.inserted_id)

# Previous code (MongoDB connection, creating collections, inserting data, etc.)

# Query Data code snippet
import pymongo

# MongoDB connection string
mongodb_url = "mongodb://localhost:27017/"

# Connect to MongoDB
client = pymongo.MongoClient(mongodb_url)

# Access a specific database (replace 'mydatabase' with your database name)
database = client["mydatabase"]

# Access the desired collections
users_collection = database["users"]
posts_collection = database["posts"]

# Example 1: Query a single document from the users collection
# Find a user with the username 'example_user'
query = {"username": "example_user"}
user = users_collection.find_one(query)
print("User found:", user)

# Example 2: Query multiple documents from the posts collection
# Find all posts authored by 'John Doe'
query = {"author": "John Doe"}
posts = posts_collection.find(query)
print("Posts authored by John Doe:")
for post in posts:
    print(post)

import pymongo

# MongoDB connection string
mongodb_url = "mongodb://localhost:27017/"

# Connect to MongoDB
client = pymongo.MongoClient(mongodb_url)

# Access a specific database (replace 'mydatabase' with your database name)
database = client["mydatabase"]

# Access the desired collections
users_collection = database["users"]
posts_collection = database["posts"]

# Example 1: Update a document in the users collection
# Update the email of the user with the username 'example_user'
query = {"username": "example_user"}
new_values = {"$set": {"email": "new_email@example.com"}}
users_collection.update_one(query, new_values)
print("User email updated successfully")

# Example 2: Delete a document from the posts collection
# Delete a post with a specific title
query = {"title": "Introduction to MongoDB"}
posts_collection.delete_one(query)
print("Post deleted successfully")

