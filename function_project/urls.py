from django.contrib import admin
from django.urls import path, include
from welcome import views as welcome_views  # welcome アプリケーションの views をインポートする
from transactions import views as transactions_views  # transactions アプリケーションの views をインポートする

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_views.welcome_page, name='welcome'),  # Welcome画面用のURLパターンを追加し、views.welcome_page をマッピング
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('transactions.urls', namespace='transactions')),
    path('income-list/', transactions_views.income_list, name='income_list'),  # 収入一覧用のビュー関数を直接マッピング
    path('expense-list/', transactions_views.expense_list, name='expense_list'),  # 支出一覧用のビュー関数を直接マッピング
]
