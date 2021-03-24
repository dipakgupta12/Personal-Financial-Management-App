from django.conf.urls import url
from financial_management_app import views


app_name = "transactions"

urlpatterns = [
    url(r"^$",views.MonthlyExpensesView.as_view(),name="detail",),
]
