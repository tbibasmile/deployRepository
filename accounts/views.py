from django.shortcuts import render, redirect
from . import forms
from django.core.exceptions import ValidationError
from .models import UserActivateTokens
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

def home(request):
    return render(request, 'accounts/home.html')

def regist(request):
    regist_form = forms.RegistForm(request.POST or None)
    if regist_form.is_valid():
        try:
            user = regist_form.save(commit=False)
            user.is_active = True  # フラグを1に設定
            user.save()
            return redirect('accounts:home')
        except ValidationError as e:
            regist_form.add_error('password', e)        
    return render(request, 'accounts/regist.html', context={'regist_form': regist_form})

def activate_user(request, token):
    try:
        user_activate_token = UserActivateTokens.objects.get(token=token)
        user = user_activate_token.user
        user.is_active = True
        user.save()
        messages.success(request, 'ユーザーが正常にアクティブ化されました。')
    except UserActivateTokens.DoesNotExist:
        messages.error(request, '無効なトークンです。')
    except Exception as e:
        messages.error(request, 'アクティブ化中にエラーが発生しました。')
    return redirect('accounts:home')
    
def user_login(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    
    login_form = forms.LoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, 'ログインが完了しました。')
                return redirect('accounts:home')
            else:
                messages.warning(request, 'ユーザがアクティブでありません')
        else:
            messages.warning(request, 'ユーザーかパスワードが間違っています')
    return render(request, 'accounts/user_login.html', context={'login_form': login_form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'ログアウトしました')
    return redirect('accounts:home')

# 新しいビュー関数を追加
def add_income(request):
    # ここに追加したいロジックを記述します
    return render(request, 'accounts/add_income.html')  # 仮の返り値として add_income.html を返します
