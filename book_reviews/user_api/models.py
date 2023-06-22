from django.db import models


# Create your models here.
class UserModel(models.Model):
    user = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    password= models.CharField(max_length=256)
    email= models.CharField(max_length=256)
    class Meta:
        db_table= "Users"