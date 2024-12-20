from django.db import models


class Supliers(models.Model):
    id_suplier = models.BigAutoField(primary_key=True)
    name_enterprise = models.CharField(max_length=50)
    data_criation = models.DateTimeField(auto_now_add=True)


class clientes(models.Model):
    id_client = models.BigAutoField(primary_key=True)
    name_client = models.CharField(max_length=50)
    requisition_day = models.IntegerField()
    data_criation = models.DateTimeField(auto_now_add=True)


class Products(models.Model):
    id_product = models.AutoField(primary_key=True)
    name_product = models.CharField(max_length=50)
    price_product = models.FloatField(max_length=200)
    data_criation = models.DateTimeField(auto_now_add=True)