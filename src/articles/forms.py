from django import forms
from django.utils.safestring import mark_safe


class ArticleForm(forms.ModelForm):
    image = forms.FileField(
            widget=forms.ClearableFileInput(attrs={'multiple': True}),
            required=False,
            help_text='Необходимое количество фото - 7',
            label=mark_safe("<strong>Фото</strong>")
            )