from decimal import Decimal
from typing import cast

from django.db import models
from django.utils import timezone


class Income(models.Model):
    """Calculates total income in a month"""
    _month = models.DateField(default=timezone.now)
    room_revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    food_and_beverage = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    other_income = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def total_income(self) -> Decimal:
        """
        This methord adds the total room_revenue, food and beverage costs, and other income to calculate total income.

        Returns:
            int
        """
        return (
            (self.room_revenue or Decimal("0"))
            + (self.food_and_beverage or Decimal("0"))
            + (self.other_income or Decimal("0"))
        )

    def __str__(self) -> str:
        """
        This methord returns the month's total income.

        Returns:
            str
        """
        return f"Date And Time = {self._month.strftime('%B - %Y')} | Total = {self.total_income()}"


class Expense(models.Model):
    """Calculates expenses in a month"""
    _month = models.DateField(default=timezone.now)
    salaries = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    rent = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    water = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    ota_commissions = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    maintenance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    other_income = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def total_expense(self) -> Decimal:
        return (
            (self.salaries or Decimal("0"))
            + (self.rent or Decimal("0"))
            + (self.water or Decimal("0"))
            + (self.ota_commissions or Decimal("0"))
            + (self.maintenance or Decimal("0"))
            + (self.other_income or Decimal("0"))
        )

    def __str__(self) -> str:
        return f"Date And Time = {self._month.strftime('%B - %Y')}  | Total Expense = {self.total_expense()}"


class Documents(models.Model):
    def __init__(self) -> None:
        self._document = models.FileField(upload_to=".bills")
        self._month = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f"Date And Time = {self._month.strftime('%B - %Y - %d')}"
