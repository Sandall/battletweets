from tastypie import fields
from tastypie.resources import ModelResource
from tweets.models import Battle, Tweet
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization

from tweets.utils import winning_tweet


class BattleResource(ModelResource):

    def dehydrate(self, bundle):
        red_mistakes_count = bundle.obj.mistakes()['red']
        blue_mistakes_count = bundle.obj.mistakes()['blue']

        bundle.data['red_mistakes_count'] = red_mistakes_count
        bundle.data['blue_mistakes_count'] = blue_mistakes_count
        bundle.data['winning_hash_tag'] \
            = winning_tweet(bundle.obj.red_corner, red_mistakes_count, bundle.obj.blue_corner, blue_mistakes_count)
        return bundle

    class Meta:
        queryset = Battle.objects.all()
        resource_name = 'battle'
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        include_resource_uri = False


class TweetResource(ModelResource):

    battle = fields.ForeignKey(BattleResource, 'battle')

    class Meta:
        queryset = Tweet.objects.all()
        resource_name = 'tweet'
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        include_resource_uri = False
