# Battle of the Tweets!

##What is battletweets?

Battletweets is an application that records the amount of spelling mistakes between two given tweets over a specified 
period of time.

##How does it work?

The application has a simple flow: firstly a user must define a battle, once defined the user can initiate the battle by
checking the 'started' flag. The battle will run until the end time is met. The winner may be queried at any point 
during and after said battle. 

Battles can be created via the Django admin area, or via the exposed REST interface. 

##How does one run it?

The application requires several things to run:
- Python 3.6 (32-bit - due to pyechant compatibility)
    - pyenchant
    - tweepy
    - django
    - django-tastypie
- python3-enchant package

For convenience, all the required run-times are provided in the Dockerfile at the project's root directory. The run this
follow the commands below. 

####Firstly, an image needs to be built:
######(make sure you've changed directory to the root of the project!)
```
$ docker build -t bt . 
```

####Secondly, the image needs to be run in a container:
```
$ docker run -d -P bt
```

####Next, found out the port the app is accessible on (in this example it's 32768):
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                     NAMES
bb8192fdd182        900288765caa        "python manage.py ..."   13 minutes ago      Up 13 minutes       0.0.0.0:32768->8000/tcp   goofy_mcnulty
```

####The app can then be queried:
######The REST interface sits behind basic auth so be sure to auth with each request!
```
$ curl -XGET -u admin:password01 -i -H 'Accept:application/json' http://192.168.99.100:32769/battle/1/
HTTP/1.0 200 OK
Date: Wed, 06 Sep 2017 19:24:33 GMT
Server: WSGIServer/0.2 CPython/3.6.2
Content-Type: application/json
Vary: Accept
Cache-Control: no-cache
X-Frame-Options: SAMEORIGIN
Content-Length: 260
{
    "blue_corner": "#LOVE_YOURSELF", 
    "blue_mistakes_count": 247, 
    "end_time": "2017-09-06T18:10:00", 
    "id": 1, 
    "red_corner": "#ReadABookDay", 
    "red_mistakes_count": 19, 
    "start_time": "2017-09-06T18:07:58.940088", 
    "started": true, 
    "winning_hash_tag": "#ReadABookDay"
}
```

####Battles can be created using POST. Sample body (application/json):
```
{
    "blue_corner": "#LOVE_YOURSELF",
    "end_time": "2017-09-06T18:10:00",
    "red_corner": "#ReadABookDay",
    "started": true
}
```

##Considerations and Shortcomings

- The default admin account is admin/password01.
- Only the amount of spelling mistakes are recorded, not density!
- The spelling checking is done against a en_US dictionary, and the tweets aren't filtered by language!
- URLs, hash tags, and email addresses are excluded from being spell checked.

