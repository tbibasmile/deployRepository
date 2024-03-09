from django.shortcuts import render, redirect, get_object_or_404
from .models import Income, Expense
from .forms import RegistForm
from django.contrib.auth.decorators import login_required

def income_list(request):
    incomes = Income.objects.all()
    return render(request, 'transactions/income_list.html', {'incomes': incomes})

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'transactions/expense_list.html', {'expenses': expenses})

def add_income(request):
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transactions:income_list')
    else:
        form = RegistForm()
    
    # バリデーションエラーがある場合はフォームを再度表示し、エラーメッセージを含める
    return render(request, 'transactions/add_income.html', {'form': form})

def edit_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        form = RegistForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('transactions:income_list')  # 編集成功後のリダイレクト
    else:
        form = RegistForm(instance=income)
    return render(request, 'transactions/edit_income.html', {'form': form})


def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = RegistForm(request.POST, instance=expense)  # インスタンスを渡す
        if form.is_valid():
            form.save()
            return redirect('transactions:expense_list')
    else:
        form = RegistForm(instance=expense)  # インスタンスを渡す
    return render(request, 'transactions/edit_expense.html', {'form': form})


def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    income.delete()
    return redirect('income_list')

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect('expense_list')

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
            # ログインしているユーザーを取得
            user = request.user
            # フォームのインスタンスにログインしているユーザーを関連付けて保存
            form.instance.user = user
            form.save()
            return redirect('transactions:expense_list')
    else:
        form = RegistForm()
    
    # バリデーションエラーがある場合はフォームを再度表示し、エラーメッセージを含める
    return render(request, 'transactions/add_expense.html', {'form': form})
