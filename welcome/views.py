from django.shortcuts import render

def welcome_page(request):
    return render(request, 'welcome/welcome.html')

def income_list(request):
    # 収入一覧の表示ロジックを実装する
    pass

def expense_list(request):
    # 支出一覧の表示ロジックを実装する
    pass
