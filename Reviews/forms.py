from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = {'text', 'rating', 'timestamp', 'user', 'product_reviewed'}
        widgets = {
            'timestamp': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'product_reviewed': forms.HiddenInput(),
            'rating': forms.Select(Review.RATING)
        }
