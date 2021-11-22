from django.contrib import admin
from content.models import UserFollows, Review, Ticket
from django.contrib.auth.models import Group

admin.site.register(UserFollows)
admin.site.register(Review)
admin.site.register(Ticket)
admin.site.unregister(Group)
admin.site.site_header = 'Administration LITReview'
admin.site.site_title = 'LITReview Admin'