from django.contrib import admin
from .models import Battle, Tweet, TweetSpellingMistake


class TweetSpellingMistakeInline(admin.StackedInline):
    model = TweetSpellingMistake
    extra = 0


class TweetInline(admin.StackedInline):
    fieldsets = [
        (None, {'fields': []})
    ]
    model = Tweet
    extra = 0

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class TweetAdmin(admin.ModelAdmin):
    inlines = [TweetSpellingMistakeInline]


class BattleAdmin(admin.ModelAdmin):
    inlines = [TweetInline]

admin.site.register(Tweet, TweetAdmin)
admin.site.register(Battle, BattleAdmin)
