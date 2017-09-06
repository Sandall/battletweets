from functools import reduce

from django.db import models
from django.utils.timezone import now

from tweets.spell_checker import check_spellings


class Battle(models.Model):
    red_corner = models.CharField(max_length=140)
    blue_corner = models.CharField(max_length=140)
    started = models.BooleanField(default=False)
    end_time = models.DateTimeField('end time')
    start_time = models.DateTimeField('start time', default=None)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.started:
            self.start_time = now()
            super().save(force_insert, force_update, using, update_fields)
            from tweets.stream_listener import start_stream
            start_stream(self)
        else:
            super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return "%s: %s vs %s %s" % (self.id, self.red_corner, self.blue_corner, "(started)" if self.started else "")

    def mistakes(self):
        red_tweets = Tweet.objects.filter(battle=self, text__contains=self.red_corner)
        blue_tweets = Tweet.objects.filter(battle=self, text__contains=self.blue_corner)
        red_mistake_count = self.mistakes_count(red_tweets)
        blue_mistake_count = self.mistakes_count(blue_tweets)
        return {"red": red_mistake_count, "blue": blue_mistake_count}

    @staticmethod
    def mistakes_count(tweets):
        counts_list = list(map(lambda x: TweetSpellingMistake.objects.filter(tweet=x).count(), tweets))
        return reduce((lambda x, y: x + y), counts_list, 0)


class TweetManager(models.Manager):
    def create_tweet(self, battle_id, text):
        tweet = self.create(battle_id=battle_id, text=text)
        return tweet


class Tweet(models.Model):
    battle = models.ForeignKey(Battle)
    text = models.CharField(max_length=140)
    objects = TweetManager()

    def __str__(self):
        return "%s: %s" % (self.id, self.text)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        checker = check_spellings(self)
        for err in checker:
            TweetSpellingMistake.objects.create_tweet_spelling_mistake(self, err.word)
            print("Detected mistake:", err.word)


class TweetSpellingMistakeManager(models.Manager):
    def create_tweet_spelling_mistake(self, tweet, word):
        tweet_spelling_mistake = self.create(tweet_id=tweet.id, word=word)
        return tweet_spelling_mistake


class TweetSpellingMistake(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    word = models.CharField(max_length=140)
    objects = TweetSpellingMistakeManager()

    def __str__(self):
        return self.word
