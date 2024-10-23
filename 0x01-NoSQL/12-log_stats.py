#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx, Display same as example
first line: x logs, x number of documents in this collection
second line: Methods
5 lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
one line with method=GET, path=/status
"""
from pymongo import MongoClient

# List of HTTP methods to check
METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection):
    """
    Provide some stats about Nginx logs stored in MongoDB
    """
    # Count total number of logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Count number of requests by HTTP method
    print("Methods:")
    for method in METHODS:
        method_count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")
    
    # Count number of requests with method=GET and path=/status
    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    # Connect to MongoDB and access the logs collection
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Print log statistics
    log_stats(nginx_collection)
