#models.py


from django.db import models
class ProductData(models.Model):
    sr_no = models.IntegerField()
    date = models.DateField()
    product_name = models.CharField(max_length=255)
    specification = models.TextField()
    customer_name = models.CharField(max_length=255)
    l1_price = models.DecimalField(max_digits=10, decimal_places=2)
    gst_percent = models.DecimalField(max_digits=5, decimal_places=2)
    gross_cost_value = models.DecimalField(max_digits=10, decimal_places=2)
    usd = models.DecimalField(max_digits=10, decimal_places=2)
    vendor1_name = models.CharField(max_length=255)
    vendor1_price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor2_name = models.CharField(max_length=255)
    vendor2_price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor3_name = models.CharField(max_length=255)
    vendor3_price = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField()

    def __str__(self):
        return self.product_name

