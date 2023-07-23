from django import forms

class ContactForms(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":"6","cols":"60",'placeholder': 'خب بگو ببینم ...'}))


class completeForm(forms.Form):
    name = forms.CharField(max_length=50)
    family = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.IntegerField()