import time
import json
from collections import namedtuple

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from threading import Thread

from tweets.models import Tweet

access_token = "1464983232-p2tY4KfCR2yoJbfSUAOdZ9QZOJkcXMkc0UnncbP"
access_token_secret = "NKISDyrVvbeuItAAMmOJ4eGkp7zQdHQkniOOISqctspYe"
consumer_key = "rtQDfamtR76NE9a8KVSpfeMMw"
consumer_secret = "AyzWEVMkuxVbMvQCqofjH1mIs33arFQlLEynoJIx5g5qw5SCYx"


class Listener(StreamListener):

    def __init__(self, battle, api=None):
        self.start_time = time.time()
        self.end_time_epoch = battle.end_time.timestamp()
        self.battle = battle
        super().__init__(api)

    def on_data(self, data):
        if time.time() < self.end_time_epoch:
            tweet = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            Tweet.objects.create_tweet(self.battle.id, tweet.text)
            print("Received Tweet for battle: %s" % self.battle.id)
            return True
        else:
            print("Closing stream...")
            return False

    def on_error(self, status):
        print(status)
        if status == 420:
            return False


def start_stream(battle):
    thread_function(battle, init_stream)
    return


def thread_function(battle, fun):
    thread = Thread(target=fun, args=(battle,))
    thread.start()


def init_stream(battle):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, Listener(battle))
    stream.filter(track=[battle.red_corner, battle.blue_corner])
