from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Goods(models.Model):
    goods_expenses = models.CharField(max_length=100, null=False, blank=True)
    goods_savings = models.CharField(max_length=100, null=False, blank=True)


class Savings(models.Model):
    sum = models.IntegerField()
    good = models.ManyToManyField(Goods)
    time_saving = models.DateTimeField(default=datetime.now())
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'good: {self.good}, price: {self.sum}, time: {self.time_saving}'


class Expenses(models.Model):
    sum = models.IntegerField()
    good = models.ManyToManyField(Goods)
    time_expenses = models.DateTimeField(default=datetime.now())
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'good: {self.good}, price: {self.sum}, time: {self.time_expenses}'
