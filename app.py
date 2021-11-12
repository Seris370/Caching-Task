from flask import Flask

from main import create_database, r, get_redis, get_disk, create_redis

api = Flask(__name__)


@api.route('/create', methods=['POST'])
def create_random_data():
    create_database()


@api.route('/view', methods=['GET'])
def get_data():
    data = None
    try:
        print("retrieving data from redis...")
        data = get_redis()
    except Exception:
        pass
    if not data:
        print("retrieving data from disk...")
        data = get_disk()
        print("saving data to redis...")
        create_redis()
    return data


if __name__ == '__main__':
    api.run()
