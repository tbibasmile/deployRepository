from django import forms
from .models import Income

class RegistForm(forms.ModelForm):
    class Meta:
        model = Income  # Income モデルを指定します
        fields = ['user', 'amount', 'description', 'date']  # Income モデルのフィールドを指定します

