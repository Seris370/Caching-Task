## Prerequisite
- Redis
- Python Redis library

## How to run
1. Start redis server

`redis-server /etc/redis/6379.conf`

2. Check redis process

`pgrep redis-server`

3. Create the database and get stats of fetching json from disk and redis

`python3 main.py`

The result will be printed to the console as follows:

```
<function create_database at 0x0000028DCB1D55E8>
Time taken: 19.43489360809326
<function create_redis at 0x0000028DCB272AF8>
Time taken: 10.452352523803711
<function get_json at 0x0000028DDB9C4168>
Time taken: 4.914074182510376
<function get_redis at 0x0000028DDB980288>
Time taken: 1.4773468971252441
```

You can check the json database at `data/database`, but it may crash.

4. Stop the redis server.

`redis-cli shutdown`

5. Clean the database.

`redis-cli flushadb`