from django import forms
from django.utils.safestring import mark_safe


class ArticleForm(forms.ModelForm):
    image = forms.FileField(
            widget=forms.ClearableFileInput(attrs={'alt': 'Text'}),
            required=False,
            label=mark_safe("<strong>Image</strong>")
            )