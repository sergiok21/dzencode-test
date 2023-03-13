from captcha.fields import CaptchaField
from django import forms

from comments.models import Comments


class CommentForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'name': 'msg',
        'id': 'msg',
        'type': 'text',
        'cols': '30',
        'rows': '5',
        'class': 'form-control',
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'msg',
        'id': 'msg',
        'type': 'text',
        'cols': '30',
        'rows': '5',
        'class': 'form-control',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'name': 'email',
        'id': 'email',
        'type': 'text',
        'class': 'form-control',
    }))
    home_page = forms.URLField(required=False, widget=forms.TextInput(attrs={
        'name': 'name',
        'id': 'homepage',
        'type': 'text',
        'class': 'form-control',
    }))
    parent_comment = forms.IntegerField(required=False)
    captcha = CaptchaField()

    class Meta:
        model = Comments
        fields = ['message', 'name', 'email', 'home_page', 'parent_comment', 'captcha']
