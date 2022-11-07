from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Goods(models.Model):
    goods_expenses = models.CharField(max_length=100, null=False, blank=True)
    goods_savings = models.CharField(max_length=100, null=False, blank=True)


class Savings(models.Model):
    sum = models.IntegerField()
    good_savings = models.ForeignKey(Goods, on_delete=models.CASCADE, default='')
    time_saving = models.DateTimeField(default=datetime.now())
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        return f'good: {self.good_savings}, price: {self.sum}, time: {self.time_saving}'


class Expenses(models.Model):
    sum = models.IntegerField()
    good_expense = models.ForeignKey(Goods, on_delete=models.CASCADE, default='')
    time_expenses = models.DateTimeField(default=datetime.now())
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        return f'good: {self.good_expense}, price: {self.sum}, time: {self.time_expenses}'

