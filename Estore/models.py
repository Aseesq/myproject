from django.db import models
from tinymce.models import HTMLField

class category(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class product(models.Model):
    name = models.CharField(max_length=100)
    description = HTMLField(null=True)
    image= models.ImageField(upload_to='image/',null=True)
    image1 = models.ImageField(upload_to='image1/',null=True)
    stock = models.IntegerField()
    price = models.IntegerField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
class siginup(models.Model):
    username=models.CharField(max_length=100,null=True)
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=30,null=True)
    contact=models.CharField(max_length=15,null=True)

    
