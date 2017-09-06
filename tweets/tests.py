from django.test import TestCase

from tweets.utils import winning_tweet


class UtilsTest(TestCase):
    def test_winning_tweet_returns_tweet_with_lowest_count(self):
        winner = winning_tweet("#Red", 10, "#Blue", 1)
        self.assertEqual(winner, "#Blue")
