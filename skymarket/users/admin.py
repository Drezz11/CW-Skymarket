from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from skymarket.users.models import User

admin.site.register(User)
#admin.site.unregister(Group)