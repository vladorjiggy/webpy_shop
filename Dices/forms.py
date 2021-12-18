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

class SearchForm(forms.ModelForm):

    name = forms.CharField(required=False)
    class Meta:
        model = Dice
        fields = ['name', 'sides']
        widgets = {
            'sides': forms.Select(choices=Dice.SIDES)
        }
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['sides'].required = False