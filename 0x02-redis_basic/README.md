Redis Basic - Backend Project

This repository contains exercises to demonstrate basic Redis operations and usage in Python, including caching and tracking function calls. These tasks are part of learning Redis basics in backend development.

Resources

Redis Crash Course Tutorial

Redis Commands

Redis Python Client

How to Use Redis with Python


Learning Objectives

1. Understand how to use Redis for basic operations.


2. Learn how to use Redis as a simple cache.


3. Implement Redis data storage and retrieval using Python.



Requirements

All files are compiled on Ubuntu 18.04 LTS using Python 3.7.

Follow pycodestyle (version 2.5) for code style.

Include documentation for all modules, classes, functions, and methods.

Ensure type annotations for all functions and coroutines.

Install Redis on Ubuntu 18.04 and use Redis in a container for local development.


Installation

1. Install Redis server:

sudo apt-get -y install redis-server
pip3 install redis


2. Update Redis config:

sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf


3. Start Redis server in the container:

service redis-server start



Project Structure

exercise.py: Contains all class implementations and methods for the tasks below.

web.py: Contains advanced tasks, implementing web caching and tracking with Redis.


Tasks

0. Writing Strings to Redis

Objective: Create a Cache class to store data in Redis. It uses a random key for data storage and can handle different data types (str, bytes, int, float).

Method:

store(data: Union[str, bytes, int, float]) -> str: Generates a random key and stores data in Redis.



Example:

cache = Cache()
key = cache.store(b"hello")
print(redis.Redis().get(key))  # Output: b'hello'

1. Reading from Redis and Recovering Original Type

Objective: Create a get method to retrieve stored data from Redis and convert it back to its original format using an optional Callable argument.

Methods:

get(key: str, fn: Callable = None) -> Any: Retrieve and convert the value.

get_str(key: str) -> str: Retrieve and convert value to string.

get_int(key: str) -> int: Retrieve and convert value to integer.



Example:

cache = Cache()
cache.store(123)
cache.get_int(key)  # Output: 123

2. Incrementing Values

Objective: Implement a system to count how many times methods of the Cache class are called.

Method:

count_calls: A decorator that tracks the call count for each method using the Redis INCR command.



Example:

cache.store(b"first")
print(cache.get(cache.store.__qualname__))  # Output: b'1'

3. Storing Lists

Objective: Track the history of function calls, storing both inputs and outputs in Redis lists.

Method:

call_history: A decorator that stores the function input parameters and output in two separate lists in Redis.



Example:

cache.store("first")
cache.store("second")
inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

4. Retrieving Lists (Replay)

Objective: Create a replay function to display the history of a function’s calls.


Example:

replay(cache.store)
# Output:
# Cache.store was called 3 times:
# Cache.store(*('foo',)) -> <key>

5. Expiring Web Cache and Tracker (Advanced)

Objective: Implement a web caching system using Redis. Cache the HTML content of a URL for 10 seconds and track how many times a URL was accessed.


Example:

get_page("http://slowwly.robertomurray.co.uk")

How to Run

Run the main files:

python3 main.py

For advanced tasks, run the web.py file:

python3 web.py


Author

This project was implemented by Martin Nyemba as part of the ALX Backend Storage curriculum.


