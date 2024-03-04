from django.contrib import admin
from django.urls import path, include
from transactions import views  # transactions アプリケーションの views をインポートする


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('transactions.urls', namespace='transactions')),  # transactionsアプリケーションのURLconfをtransactionsという名前空間で含める
    path('income-list/', views.income_list, name='income_list'),  # '/income-list/' を views.income_list にマッピング
    path('expense-list/', views.expense_list, name='expense_list'),  # '/expense-list/' を views.expense_list にマッピング
]