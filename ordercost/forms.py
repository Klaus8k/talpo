from django import forms

PAPER = [(130, '130'),  # Переменную берем из модуля бизнеслогики
         (170, '170'),
         (300, '300')]


class OffsetForms(forms.Form):
    calculation = forms.IntegerField(min_value=1)
    size_x = forms.IntegerField(min_value=25)
    size_y = forms.IntegerField(min_value=25)
    weigth_paper = forms.ChoiceField(choices=PAPER)
