from django.db import models

class category(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    stock = models.IntegerField()
    price = models.IntegerField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
