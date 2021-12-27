from django import forms
from .models import Dice


class DiceForm(forms.ModelForm):
    image = forms.ImageField()
    product_info = forms.FileField()

    class Meta:
        model = Dice
        fields = ['name', 'description', 'colour', 'sides', 'prize', 'image', 'product_info']
        widgets = {
            'sides': forms.Select(choices=Dice.SIDES),
        }
