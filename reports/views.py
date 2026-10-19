from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseBase
from django.shortcuts import render

from .calculations import calculate_the_report
from .models import Expense, Income


class Views:
    @staticmethod
    @login_required
    def managers_report(request: HttpRequest) -> HttpResponseBase:
        managers = request.user.groups.filter(name="Managers")  # pyright: ignore[reportAttributeAccessIssue]
        income = Income()
        income_total = income.total_income()
        expense = Expense()
        expense_total = expense.total_expense()
        gop, base_fee, incentive_fee, remaining = calculate_the_report(
            income_total, expense_total
        )
        if managers:
            return render(
                request,
                "reports/managers-report",
                {
                    "gop": gop,
                    "base_fee": base_fee,
                    "incentive_fee": incentive_fee,
                    "remaining": remaining,
                },
            )
        else:
            return render(request, "reports/access-denied.html")

    @staticmethod
    @login_required
    def owners_report(request: HttpRequest) -> HttpResponseBase:
        owners = request.user.groups.filter(name="Owners")  # pyright: ignore[reportAttributeAccessIssue]
        income: Income = Income()
        income_total = income.total_income
        expense: Expense = Expense()
        expense_total = expense.total_expense
        gop, base_fee, incentive_fee, remaining = calculate_the_report(
            income_total, expense_total
        )
        if owners:
            return render(
                request,
                "reports/owners-report",
                {
                    "gop": gop,
                    "base_fee": base_fee,
                    "incentive_fee": incentive_fee,
                    "remaining": remaining,
                },
            )
        else:
            return render(request, "reports/access-denied.html")

    @staticmethod
    def home_page(request: HttpRequest) -> HttpResponseBase:
        return render(request, "reports/index.html")

