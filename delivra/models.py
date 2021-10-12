from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Product: {self.product} | Quantity:  {self.quantity} | Amount: {self.quantity * self.product.price}"

    @property
    def total_price(self):
        return self.quantity * self.product.price
