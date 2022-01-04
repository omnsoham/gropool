from django.contrib import admin
from _List.models import MyList, MyListItems
# Register your models here.
@admin.register(MyList)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['listId', 'listGroupId', 'listName', 'listCreator']
@admin.register(MyListItems)
class MyListItemsAdmin(admin.ModelAdmin):
    list_display = ['listitemId', 'listMaster', 'listItemName']
