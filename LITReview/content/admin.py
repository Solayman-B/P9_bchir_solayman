from django.contrib import admin
from content.models import UserFollows, Review, Ticket

admin.site.register(UserFollows)
admin.site.register(Review)
admin.site.register(Ticket)