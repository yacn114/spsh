from django import forms
from hesab.models import User

class UserForms(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField(widget=forms.TextInput(attrs={'value':123}))
    githublink = forms.CharField()
