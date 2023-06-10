from django import forms
class WalletMoves(forms.Form):
    balance = forms.IntegerField()
    user_id = forms.CharField(max_length=20)
