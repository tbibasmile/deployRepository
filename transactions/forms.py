from django import forms
from .models import Income, Expense

class RegistForm(forms.ModelForm):
    class Meta:
        model = Income  # または Expense
        fields = ['date', 'description', 'amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'id': 'id_date'})
        self.fields['description'].widget.attrs.update({'id': 'id_description'})
        self.fields['amount'].widget.attrs.update({'id': 'id_amount'})

    # バリデーションメソッドのオーバーライド
    def clean(self):
        cleaned_data = super().clean()
        # バリデーションルールを追加する場合、ここで検証する
        # 例えば、金額がマイナスでないかをチェックするなど
        return cleaned_data
