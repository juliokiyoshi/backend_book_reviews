from django.db import models
from user_api.models import UserModel

class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    user= models.ForeignKey(UserModel, related_name="id",on_delete=models.CASCADE)
    book_name = models.CharField(max_length=256)
    user_review= models.CharField(max_length=2048)
    book_rating= models.FloatField(default=0.0)
    class Meta:
        db_table= "review"