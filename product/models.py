from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(MPTTModel, TimeStampedModel):
    name = models.CharField(max_length=128)
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    title = models.CharField(max_length=128)
    product_code = models.CharField(max_length=128)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name='products')

