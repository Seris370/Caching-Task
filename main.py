import json
import random
import time
import redis

file_path = "data/database"
r = redis.Redis()
data = {i: random.random() for i in range(10000000)}


def create_database():
    with open(file_path, 'w') as f:
        json.dump(data, f)


def create_redis():
    value = json.dumps(data)
    r.set("data", value)


def get_disk():
    with open(file_path, 'r') as f:
        response = "".join(f.readlines())
        return response


def get_redis():
    response = r.get("data")
    return response


def timing(func):
    print(func)
    start_time = time.time()
    func()
    end_time = time.time()
    print("Time taken:", end_time - start_time)


if __name__ == '__main__':
    timing(create_database)
    timing(create_redis)
    timing(get_disk)
    timing(get_redis)
