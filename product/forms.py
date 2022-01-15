from django import forms

class ProdForm(forms.Form):
    name = forms.CharField(max_length=100)
    weight = forms.IntegerField()
    price = forms.IntegerField()
