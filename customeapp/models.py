from django.db import models

# Create your models here.
class FLIGHTS(models.Model):
    flight_id=models.CharField(max_length=200)
    flight_name=models.CharField(max_length=200)
    source=models.CharField(max_length=200)
    destination=models.CharField(max_length=200)
    departutre_time=models.DateTimeField()
    arrival_time=models.DateTimeField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    total_seats=models.IntegerField()
    flight_type=models.CharField(max_length=200)
    food_supply=models.BooleanField(default=False)



    



    # def __str__(self):
    #     return f"{self.name} ({self.flight_id})"
    





    

