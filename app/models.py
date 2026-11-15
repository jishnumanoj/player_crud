from django.db import models


# Create your models here.
class Player(models.Model):
    name=models.CharField(max_length=200)
    age=models.PositiveBigIntegerField()
    
    SPORTS=[
        ("cricket","cricket"),
        ("chess","chess"),
        ("football","football"),
        ("hockey","hockey")
    ]
    sport=models.CharField(max_length=200,choices=SPORTS)
    role=models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200)

    