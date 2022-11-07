from django.forms import ModelForm
from .models import Savings, Expenses, Goods


class SavingsForm(ModelForm):
    class Meta:
        model = Savings
        fields = ['sum', 'good_savings', 'time_saving', 'user_id']


class ExpensesForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['sum', 'good_savings', 'time_saving', 'user_id']


class GoodsForm(ModelForm):
    class Meta:
        model = Goods
        fields = ['goods_expenses', 'goods_savings']
