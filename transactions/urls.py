from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('income/', views.income_list, name='income_list'),
    path('income/add/', views.add_income, name='add_income'),
    path('income/<int:pk>/edit/', views.edit_income, name='edit_income'),
    path('income/<int:pk>/delete/', views.delete_income, name='delete_income'),
    path('expense/', views.expense_list, name='expense_list'),
    path('expense/add/', views.add_expense, name='add_expense'),
    path('expense/<int:pk>/edit/', views.edit_expense, name='edit_expense'),
    path('expense/<int:pk>/delete/', views.delete_expense, name='delete_expense'),
]
