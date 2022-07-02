from django import forms

PAPER = [(130, '130'),  # Переменную берем из модуля бизнеслогики
         (170, '170'),
         (300, '300')]


class OffsetForms(forms.Form):
    # переопределение инит метода для изменения предупреждения
    def __init__(self, *args, **kwargs):
        super(OffsetForms, self).__init__(*args, **kwargs)
        self.fields['weigth_paper'].error_messages = {'required': "Обязательное поле"}

    calculation = forms.IntegerField(min_value=1)
    size_x = forms.IntegerField(min_value=25)
    size_y = forms.IntegerField(min_value=25)
    weigth_paper = forms.ChoiceField(choices=PAPER)
