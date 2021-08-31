from django.forms import ModelForm

from employees.models import Review


class ReviewCreateForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
