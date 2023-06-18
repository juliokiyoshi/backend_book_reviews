from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_name = models.CharField(max_length=256)
    book_resume= models.CharField(max_length=1028)
    book_rating= models.FloatField(default=0.0)
    class Meta:
        db_table= "review"