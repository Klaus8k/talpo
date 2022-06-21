from django import forms


class OffsetForms(forms.Form):
    circulation = forms.IntegerField(min_value=1)
    size_x = forms.IntegerField(min_value=25)
    size_y = forms.IntegerField(min_value=25)
    weith_paper = forms.ChoiceField(choices = [(130,'130'), # Переменную берем из модуля бизнеслогики
                                               (170,'170'),
                                               (300,'300')])