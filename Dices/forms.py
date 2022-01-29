from django import forms
from .models import Dice


class DiceForm(forms.ModelForm):
    image = forms.ImageField()
    product_info = forms.FileField()
    class Meta:
        model = Dice
        fields = ['name', 'description', 'colour', 'sides', 'prize', 'image', 'product_info']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'colour': forms.TextInput(attrs={'class': 'form-control'}),
            'prize': forms.NumberInput(attrs={'class': 'form-control'}),
            'superuser': forms.HiddenInput(),
            'sides': forms.Select(choices=Dice.SIDES, attrs={'class': 'form-control'}),
        }
    field_order = ['name', 'description', 'colour', 'prize', 'sides', 'image', 'product_info']

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
