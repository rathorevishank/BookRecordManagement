from django.db import models

# Create your models here.
class Book(models.Model):
    picture=models.ImageField(upload_to='images/',default="./media/images/image.jpg") 
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    rating=models.FloatField(default=0.0)
    description=models.TextField(default='Default Description')
    

    def __str__(self):
        return self.title