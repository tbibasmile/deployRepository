from django.urls import path
from . import views
from accounts.views import activate_user  # アクティベーション用のビューをインポート

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('regist', views.regist, name='regist'),
    path('activate_user/<uuid:token>', views.activate_user, name='activate_user'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('activate_user/<str:username>/', activate_user, name='activate_user'),  # アクティベーション用のURLパターンを追加
    path('add_income/', views.add_income, name='add_income'),  # 'add_income' という名前のパターンを追加

]