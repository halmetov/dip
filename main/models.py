from django.db import models


class Uslug(models.Model):
    name = models.CharField(max_length=100000)
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'Uslug'
        
class Gorod(models.Model):
    name = models.CharField(max_length=100000)
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'Gorod'

class Cruise(models.Model):
    id = models.AutoField(primary_key=True)
    id_uslug = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Booking = models.BooleanField()


    class Meta:
        db_table = 'Cruise'

class Booking(models.Model):
    id= models.AutoField(primary_key=True)
    date_booking = models.DateTimeField(auto_now_add=True)
    id_cruise = models.IntegerField()

    class Meta:
        db_table = 'Booking'
