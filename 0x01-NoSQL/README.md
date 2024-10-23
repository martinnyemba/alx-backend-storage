# NoSQL

Overview

In this project, we will explore NoSQL databases, specifically focusing on MongoDB. NoSQL databases differ from traditional SQL databases in that they allow for more flexible and scalable data storage, making them ideal for handling large volumes of unstructured or semi-structured data.

We will cover the following topics:

1. What NoSQL is and how it differs from SQL.


2. ACID properties and their relevance in NoSQL.


3. Different types of NoSQL databases.


4. How to perform basic operations like querying, inserting, updating, and deleting data in a MongoDB NoSQL database.


5. Using Python and PyMongo to interact with a MongoDB database.



By the end of this project, you will be able to install MongoDB, perform CRUD operations, and write Python scripts to interface with MongoDB.

Objectives

Understand the concepts behind NoSQL databases.

Learn the benefits and use cases of NoSQL.

Install and configure MongoDB.

Perform CRUD operations using MongoDB shell commands.

Interact with MongoDB using Python and the PyMongo library.


Installing Dependencies

MongoDB Installation (Ubuntu 18.04)

To install MongoDB on Ubuntu 18.04, follow the steps below:

1. Import the MongoDB GPG key:

wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -


2. Add MongoDB repository:

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list


3. Update the package database:

sudo apt-get update


4. Install MongoDB:

sudo apt-get install -y mongodb-org


5. Start the MongoDB service:

sudo service mongod start


6. Verify the installation:

mongo --version



Install PyMongo (Python MongoDB Driver)

To interact with MongoDB using Python, we need to install the PyMongo library.

1. Install PyMongo using pip:

pip3 install pymongo


2. Verify PyMongo installation:

python3 -c "import pymongo; print(pymongo.__version__)"



After completing these steps, your environment should be set up to use MongoDB with Python.

To address the tasks outlined, here are the solutions for each based on the learning objectives:

Task 0: List all databases

A script to list all databases in MongoDB can be written as follows:

// 0-list_databases
show dbs

This can be executed by piping it to the MongoDB command line interface:

cat 0-list_databases | mongo

Task 1: Create or use a database

To create or use a database named my_db, the following script will work:

// 1-use_or_create_database
use my_db

You can execute it by piping it into the MongoDB shell:

cat 1-use_or_create_database | mongo

Task 2: Insert a document into a collection

This script inserts a document with the attribute name set to "Holberton school" into the collection school:

// 2-insert
db.school.insertOne({ name: "Holberton school" })

Run it with:

cat 2-insert | mongo my_db

Task 3: List all documents

To list all documents in the collection school:

// 3-all
db.school.find().pretty()

Execute with:

cat 3-all | mongo my_db

Task 4: List all matching documents

List all documents in school with name equal to "Holberton school":

// 4-match
db.school.find({ name: "Holberton school" }).pretty()

Execute it:

cat 4-match | mongo my_db

Task 5: Count documents

To count the number of documents in the collection school:

// 5-count
db.school.countDocuments()

Run with:

cat 5-count | mongo my_db

Task 6: Update a document

This script updates all documents in school where name is "Holberton school" by adding an address field:

// 6-update
db.school.updateMany({ name: "Holberton school" }, { $set: { address: "972 Mission street" } })

Execute:

cat 6-update | mongo my_db

Task 7: Delete documents by match

To delete all documents where name is "Holberton school":

// 7-delete
db.school.deleteMany({ name: "Holberton school" })

Run with:

cat 7-delete | mongo my_db

Task 8: List all documents in Python

Here is the Python function that lists all documents in a collection:

#!/usr/bin/env python3
from pymongo import MongoClient

def list_all(mongo_collection):
    """List all documents in a collection."""
    return list(mongo_collection.find()) if mongo_collection else []

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))

Save it in a file, and run it using:

python3 8-main.py

Task 9: Insert a document in Python

Here is the Python function that inserts a new document in the collection based on kwargs:

#!/usr/bin/env python3
from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """Insert a new document into a collection based on kwargs."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    new_school_id = insert_school(school_collection, name="Holberton School", address="972 Mission street")
    print("New document ID: {}".format(new_school_id))

Run this script to insert a document:

python3 9-main.py

With these scripts, you can handle common MongoDB operations using both shell commands and Python with PyMongo.
