from django import forms

class CommentForms(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":"6","cols":"40",'placeholder': 'نظر خود را بنوسید ...'}))
