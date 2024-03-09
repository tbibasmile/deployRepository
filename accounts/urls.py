from django.urls import path
from . import views
from accounts.views import activate_user  # アクティベーション用のビューをインポート

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('regist/', views.regist, name='regist'),  # / を追加してパスの形式を統一します
    path('activate_user/<uuid:token>/', views.activate_user, name='activate_user'),  # / を追加してパスの形式を統一します
    path('user_login/', views.user_login, name='user_login'),  # / を追加してパスの形式を統一します
    path('user_logout/', views.user_logout, name='user_logout'),  # / を追加してパスの形式を統一します
    path('add_income/', views.add_income, name='add_income'),  # / を追加してパスの形式を統一します
]
