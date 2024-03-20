from django.forms import ModelForm
from django import forms
from hesab.models import User
class ContactForms(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":"6","cols":"60",'placeholder': 'خب بگو ببینم ...'}))


class completeForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name' ,'last_name' ,'phone' ,'githublink']