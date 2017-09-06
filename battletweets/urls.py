from django.conf.urls import include, url
from django.contrib import admin
from django.urls import reverse
from django.views.generic import RedirectView

from tweets.resources import BattleResource, TweetResource

battle_resource = BattleResource()
tweet_resource = TweetResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(battle_resource.urls)),
    url(r'^', include(tweet_resource.urls)),
    url(r'^$', RedirectView.as_view(url='/admin')),
]
