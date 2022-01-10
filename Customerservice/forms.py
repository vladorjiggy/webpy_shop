from django import forms
from Reviews.models import Review
from Dices.models import Dice


class ReviewEditForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {'text', 'rating'}
        widgets = {
            'timestamp': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'product_reviewed': forms.HiddenInput(),
            'rating': forms.Select(choices=Review.RATING)
        }


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Dice
        fields = {'name', 'description', 'colour', 'sides', 'prize', 'image'}
        widgets = {
            'timestamp': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }
