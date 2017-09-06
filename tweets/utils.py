def _compare(a, b):
    return (a > b) - (a < b)


def winning_tweet(red_tweet, red_tweet_mistakes_count, blue_tweet, blue_tweet_mistakes_count):
    cmp = _compare(blue_tweet_mistakes_count, red_tweet_mistakes_count)
    if cmp == 1:
        return red_tweet
    elif cmp == 0:
        return 'Draw'
    else:
        return blue_tweet
