from django import forms
class WalletMoves(forms.Form):
    balance = forms.CharField()
    user_id = forms.CharField(max_length=20)
