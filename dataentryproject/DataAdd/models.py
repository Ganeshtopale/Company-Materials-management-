from django.db import models

class Product(models.Model):
    customer_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    specification = models.TextField()
    target_price = models.DecimalField(max_digits=10, decimal_places=2)
    uom = models.CharField(max_length=50)  # Unit of Measurement
    qty = models.IntegerField()
    vendor_1 = models.DecimalField(max_digits=10, decimal_places=2)
    vendor_2 = models.DecimalField(max_digits=10, decimal_places=2)
    vendor_3 = models.DecimalField(max_digits=10, decimal_places=2)
    vendor_4 = models.DecimalField(max_digits=10, decimal_places=2)
    l1_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    gst_percent = models.DecimalField(max_digits=5, decimal_places=2)
    gst_value = models.DecimalField(max_digits=10, decimal_places=2)
    p_f = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    freight_vendor_to_idi = models.DecimalField(max_digits=10, decimal_places=2)
    freight_idi_to_customer = models.DecimalField(max_digits=10, decimal_places=2)
    quoted_price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    actual_profit = models.DecimalField(max_digits=10, decimal_places=2)
    quotation_no = models.CharField(max_length=100)
    quotation_date = models.DateField()
    purchase_order_no = models.CharField(max_length=100)
    purchase_order_date = models.DateField()
    del_target_date = models.DateField()
    actual_delivery_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.product_name
