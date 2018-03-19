# message-center
A message center app built using Django Channels

This is a messaging app built using Django Channels. Users may create rooms and post messages in it. Rooms and messages are persisted in sqlite db and can be viewed new and returning users.

## How to run
In  order to run this app, you'll need Python and [Redis](https://redis.io/topics/quickstart).
- Clone repo and switch to project dir
- Install requirements: `pip install -r requirements.txt`
- Migrate db: `python manage.py migrate`
- Run redis server: `redis-server`
- Run local server: `python manage.py runserver`
