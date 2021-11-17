

from Store.models import ReviewRating
from django import forms


class Reviewform(forms.ModelForm):
    class Meta:
        model=ReviewRating
        fields=['subject','rating','review']
