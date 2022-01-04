from django.db import models
from django.contrib.auth.models import User, AbstractUser   
from Profile.static.profilepics.profunction import randomfood
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
validate_email = RegexValidator(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', 'Enter a valid email address.')

# Create your models here.
class UserInfo(AbstractUser):
    username = models.CharField(max_length=20, unique= True)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=50, validators= [validate_email], primary_key = True)
    zipcode = models.CharField(max_length=5)
    profilepic = models.ImageField(randomfood)
    description = models.CharField(max_length=200)
    REQUIRED_FIELDS = ('password','email','zipcode', 'profilepic')
    USERNAME_FIELD = ('username')

WEEKDAYS = (  
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    ('6', 'Saturday'),
    ('7', 'Sunday'),
)

SHOPS = [
    ('Costco', 'Costco'),
    ('Target', 'Target'),
    ('Walmart', 'Walmart'),
    ('Safeway', 'Safeway'),
    ('New India Bazaar', 'New India Bazaar'),
]
class MyGroup(models.Model):
    groupId = models.AutoField(primary_key=True)
    groupName = models.CharField(max_length=20, verbose_name='Group Name', unique=True)
    groupDescription = models.CharField(max_length=200, verbose_name= 'Group Description')
    dayOfDelivery = models.CharField(max_length=10, verbose_name= 'Day Of Grocery Shopping', choices=WEEKDAYS)
    shopId = models.CharField( max_length=50, verbose_name= 'Shops', choices=SHOPS, blank=True)
    addshop = models.CharField(max_length= 50, verbose_name= "Can't find your shop?", blank=True)
    zipcode = models.CharField(max_length=5, verbose_name='Zipcode')
#    def save(self,*args,**kwargs):
#        created = not self.pk
#        super().save(*args,**kwargs)
#        if created:
#            Cal.objects.create(user=self)

class FormedGroup(models.Model):
    formedGroupId = models.AutoField(primary_key=True)
    userEmail = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
    userGroupID = models.ForeignKey(MyGroup, on_delete = models.CASCADE)

#class GroceryList(model.Model):

