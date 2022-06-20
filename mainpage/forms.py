from django import forms


class MathForm(forms.Form):
    x = forms.CharField(label='x', max_length=10)
    y = forms.CharField(label='y', max_length=10)