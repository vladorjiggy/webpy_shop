from django import forms
from .models import Dice


class DiceForm(forms.ModelForm):

    image = forms.ImageField()
    class Meta:
        model = Dice
        fields = ['name', 'description', 'colour', 'sides', 'prize', 'image']
        widgets = {
            'sides': forms.Select(choices=Dice.SIDES),
        }