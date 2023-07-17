from django.contrib import admin
from .models import Ann, UserReply


@admin.register(Ann)
class AnnAdmin(admin.ModelAdmin):
    model = Ann

@admin.register(UserReply)
class UserReplyAdmin(admin.ModelAdmin):
    model = UserReply
