from django.db import models


# Create your models here.
class ParetoRate(models.Model):
    customer_id = models.CharField(max_length=20)
    Pareto_rate = models.FloatField()
    customer_count = models.FloatField()


class rfm(models.Model):
    customer_id = models.CharField(max_length=20)
    r_data = models.IntegerField()
    f_data = models.IntegerField()
    m_data = models.FloatField()
    customer_type = models.CharField(max_length=20)


class visualizationdata01(models.Model):
    year = models.CharField(max_length=5)
    sales = models.FloatField()
    profit = models.FloatField()
    profitrate = models.FloatField()
    count = models.IntegerField()
    numberOrder = models.IntegerField()
    averageDiscount = models.FloatField()
    guestListPrice = models.FloatField()


class visualizationdata01_month(models.Model):
    year = models.CharField(max_length=5)
    month = models.IntegerField()
    sales = models.FloatField()
    count = models.IntegerField()
    profit = models.FloatField()


class segment_datatable(models.Model):
    region = models.CharField(max_length=5)
    province = models.CharField(max_length=5)
    city = models.CharField(max_length=5)
    cutomer_type = models.CharField(max_length=5)
    count = models.IntegerField()


class category_saleDataTable(models.Model):
    year = models.CharField(max_length=5)
    category = models.CharField(max_length=8)
    subCategory = models.CharField(max_length=8)
    sale = models.FloatField()
    profit = models.FloatField()


class shipData(models.Model):
    shiplevel = models.CharField(max_length=5)
    shipregion = models.CharField(max_length=5)
    shipDay = models.FloatField()
    shipYear = models.CharField(max_length=5)
    shipNumber = models.IntegerField()