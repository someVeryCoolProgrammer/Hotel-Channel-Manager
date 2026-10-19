from decimal import Decimal
from typing import cast

from django.db import models


class Income(models.Model):
    """Calculates total income in a month"""

    def __init__(self) -> None:
        self.month = models.DateField()
        self.room_revenue = models.DecimalField(max_digits=12, decimal_places=2)
        self.food_and_beverage = models.DecimalField(max_digits=12, decimal_places=2)
        self.other_income = models.DecimalField(max_digits=12, decimal_places=2)

    def total_income(self) -> Decimal:
        """
        This methord adds the total room_revenue, food and beverage costs, and other income to calculate total income.

        Returns:
            int
        """
        room: Decimal = cast(Decimal, self.room_revenue)
        food_and_drinks: Decimal = cast(Decimal, self.food_and_beverage)
        other: Decimal = cast(Decimal, self.other_income)
        return room + food_and_drinks + other

    def __str__(self) -> str:
        """
        This methord returns the month's total income income.

        Returns:
            str
        """
        return f"Date And Time = {self.month.strftime('%B - %Y')} | Total = {self.total_income()}"  # pyright: ignore[reportAttributeAccessIssue]


class Expense(models.Model):
    """Calculates expenses in a month"""

    def __init__(self) -> None:
        self.month = models.DateField()
        self.salaries = models.DecimalField(max_digits=12, decimal_places=2)
        self.rent = models.DecimalField(max_digits=12, decimal_places=2)
        self.water = models.DecimalField(max_digits=12, decimal_places=2)
        self.ota_commissions = models.DecimalField(max_digits=12, decimal_places=2)
        self.maintenance = models.DecimalField(max_digits=12, decimal_places=2)
        self.other_costs = models.DecimalField(max_digits=12, decimal_places=2)

    def total_expense(self) -> Decimal:
        salaries: Decimal = cast(Decimal, self.salaries)
        rent: Decimal = cast(Decimal, self.rent)
        water: Decimal = cast(Decimal, self.water)
        ota: Decimal = cast(Decimal, self.ota_commissions)
        maintenance: Decimal = cast(Decimal, self.maintenance)
        other: Decimal = cast(Decimal, self.other_costs)
        return salaries + rent + water + ota + maintenance + other

    def __str__(self) -> str:
        return f"Date And Time = {self.month.strftime('%B - %Y')}  | Total Expense = {self.total_expense()}"  # pyright: ignore[reportAttributeAccessIssue]


class Documents(models.Model):
    def __init__(self) -> None:
        self.document = models.FileField(upload_to=".bills")
        self.month = models.DateField()

    def __str__(self) -> str:
        return f"Date And Time = {self.month.strftime('%B - %Y - %d')}"  # pyright: ignore[reportAttributeAccessIssue]
