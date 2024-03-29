from django import forms
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser, Expense

class RegistForm(forms.ModelForm):
    user_name = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('user_name', 'email', 'password')
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('パスワードが異なります')
    
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.CharField(label="メールアドレス")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput())

class ExpenseForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all(), label='ユーザー')

    class Meta:
        model = Expense
        fields = ['user', 'amount', 'description', 'date']
