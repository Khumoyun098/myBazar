from django.db import models
from django.contrib.auth.models import User

import datetime


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    date = models.DateField(editable=True, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.cost}"

    @property
    def from_day(self):
        today = datetime.date.today()
        prev = self.date
        diff = today-prev
        return diff.days

