from django.db import models


PRICE_CHOICES = {
    "clearance":"Clearance (.97)",  # Ends in .97
    "manager-discounts":"Manager Special (.88 or .00)",  # Ends in .88 or .00
    "last-batch":"Last Batch (*)",  # Has an asterisk (*) at the end
    "regular":"Regular Price",  # Ends in a 9
}

UNITS_CHOICES = {
    "lb":"lb",
    "oz": "oz",
    "pt": "pt",
    "gal": "gal",
    "fl oz": "fl. oz.",
    "kg":"kg",
    "g":"g",
    "mg":"mg",
    "l":"l",
    "ml":"mL",
    "km":"km",
    "m":"m",
}


class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


# Create your models here.
class Product(models.Model):
    product_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_sku = models.CharField(max_length=100)
    product_upc = models.CharField(max_length=100)
    product_weight = models.DecimalField(max_digits=5, decimal_places=2)
    product_weight_units = models.CharField(max_length=100, choices=UNITS_CHOICES.items())
    product_status = models.CharField(max_length=100, choices=PRICE_CHOICES.items())

    image = models.ImageField(upload_to=f'products/', null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_history(self):
        return PriceHistory.objects.filter(parent_product=self.pk)

    def __str__(self):
        return f"{self.product_brand} - {self.product_name}"


class Store(models.Model):
    owner = models.CharField(max_length=100)
    store_name = models.CharField(max_length=255)
    store_address = models.CharField(max_length=255)
    store_city = models.CharField(max_length=255)
    store_provence = models.CharField(max_length=255)
    store_postal_code = models.CharField(max_length=255)
    store_country = models.CharField(max_length=255)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name


class PriceHistory(models.Model):
    parent_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.IntegerField()  # -1 means alot, positive int is actual quantity
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parent_product.product_name} ({self.price})"
