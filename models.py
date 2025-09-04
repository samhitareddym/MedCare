from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)

    class Meta:
        db_table="contact"


class Client(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=500)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)

    class Meta:
        db_table="client"


class Service(models.Model):
    service_name=models.CharField(max_length=100)
    service_price=models.CharField(max_length=100)
    hours=models.CharField(max_length=100)
    image=models.ImageField()


class Staff(models.Model):
    staffid=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    class Meta:
        db_table="staff"


class Cart(models.Model):
    service=models.ForeignKey(Service ,on_delete=models.CASCADE)
    client=models.ForeignKey(Client ,on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    status=models.IntegerField(default=0)


    class Meta:
        db_table="cart"



