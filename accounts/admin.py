# accounts/admin.py

from django.contrib import admin
from .models import CustomUser, Income, Expense, UserActivateTokens

# Usersモデルの登録
admin.site.register(CustomUser)

# Incomeモデルの登録
admin.site.register(Income)

# Expenseモデルの登録
admin.site.register(Expense)

# UserActivateTokensモデルの登録
admin.site.register(UserActivateTokens)
