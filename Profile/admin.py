from django.contrib import admin
from .models import UserInfo, FormedGroup, MyGroup
# Register your models here.

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "email", "zipcode"]
@admin.register(MyGroup)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["groupId", "groupDescription", "dayOfDelivery", "zipcode"]