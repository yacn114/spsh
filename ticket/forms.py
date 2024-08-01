from django import forms

class ContactForms(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":"6","cols":"60",'placeholder': 'خب بگو ببینم ...'}))

