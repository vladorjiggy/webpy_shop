from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {'title', 'text', 'rating'}
        widgets = {
            'rating': forms.Select(choices=Review.RATING),
            'timestamp': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'product_reviewed': forms.HiddenInput()
        }


