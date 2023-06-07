from django import forms
from hesab.models import User

class UserForms(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    githublink = forms.CharField()

class ContactForms(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":"6","cols":"60",'placeholder': 'خب بگو ببینم ...'}))
