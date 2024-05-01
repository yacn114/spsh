from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms
from hesab.models import User
class ContactForms(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":"6","cols":"60",'placeholder': 'خب بگو ببینم ...'}))


class completeForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name' ,'last_name' ,'phone' ,'githublink']
    # def clean_phone(self):
    #     phone = str(self.cleaned_data.get('phone'))
    #     if not phone.startswith('09'):
    #         raise ValidationError('شماره تلفن باید با 09 شروع شود.')
    #     return phone
    def __init__(self, *args, **kwargs):
        super(completeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['phone'].required = True