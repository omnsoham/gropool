from django.db import models
from Profile.models import MyGroup, UserInfo
# Create your models here.
class MyList(models.Model):
    listId = models.AutoField(primary_key=True)
    listGroupId = models.ForeignKey(MyGroup, on_delete= models.CASCADE)
    listName = models.CharField(max_length=200, verbose_name='List Name', unique=True)
    listCreator = models.ForeignKey(UserInfo, on_delete= models.CASCADE)

class MyListItems(models.Model):
    listitemId = models.AutoField(primary_key=True)
    listMaster = models.ForeignKey(MyList, on_delete= models.CASCADE)
    listItemName = models.TextField(verbose_name= 'New List Item')