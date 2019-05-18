from django.contrib import admin

# Register your models here.

from .models import UserProfileInfo, Membership, Subject
# Register your models here.
admin.site.register(UserProfileInfo)

admin.site.register(Membership)

admin.site.register(Subject)