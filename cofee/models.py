from django.db import models



class cofee(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=255)
    
    
    
    def __str__(self):
        return self.name
    
    
class Register(models.Model):
    Username = models.CharField(max_length=100)
    Email_id = models.EmailField(max_length=100)
    Password = models.CharField(max_length=500)
    
    def __str__(self):
        return self.Username