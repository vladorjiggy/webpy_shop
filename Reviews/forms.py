from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {'title', 'text', 'rating'}
        widgets = {
            'rating': forms.Select(choices=Review.RATING, attrs={'class': 'form-control'}),
            'timestamp': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'product_reviewed': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }
    field_order = ['rating', 'title', 'text']

class ReviewEditForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {'title', 'text', 'rating'}
        widgets = {
            'rating': forms.Select(choices=Review.RATING, attrs={'class': 'form-control'}),
            'timestamp': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'product_reviewed': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }
    field_order = ['rating', 'title', 'text']