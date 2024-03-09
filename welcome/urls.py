from django.contrib import admin
from django.urls import path, include
from welcome import views as welcome_views  # welcome アプリケーションの views をインポートする

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_views.welcome_page, name='welcome'),  # Welcome画面用のURLパターンを追加し、views.welcome_page をマッピング
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('transactions.urls', namespace='transactions')),
    path('income-list/', include('transactions.urls')),  # 収入一覧用のURLパターンを transactions アプリケーション内のURLconfから include
    path('expense-list/', include('transactions.urls')),  # 支出一覧用のURLパターンを transactions アプリケーション内のURLconfから include
]
