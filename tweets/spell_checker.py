import re

from enchant.checker import SpellChecker
from enchant.tokenize import EmailFilter, URLFilter, Filter


def check_spellings(tweet):
    checker = SpellChecker("en_US", filters=[EmailFilter, URLFilter, HashTagFilter])
    checker.set_text(tweet.text)
    return checker


class HashTagFilter(Filter):
    _pattern = re.compile(r"#(\w+)")

    def _skip(self, word):
        if self._pattern.match(word):
            return True
        return False
