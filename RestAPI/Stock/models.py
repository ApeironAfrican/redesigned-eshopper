from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField(default='Product description.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
