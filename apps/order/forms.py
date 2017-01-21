#-*-coding:utf8-*-

from django import forms
from .models import SimpleOrder


class SimpleOrderForm(forms.ModelForm):
    phone = phone_number = forms.RegexField(widget=forms.TextInput(attrs={'placeholder': u'Ваш телефон'}),
                                            regex=r'^\+?1?\d{9,15}$',
                                            error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    class Meta:
        model = SimpleOrder
        exclude = ('basket',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':u'Ваше ммя'}),
            'comment': forms.Textarea(attrs={'placeholder': u'Коментарий'}),
            'country': forms.TextInput(attrs={'placeholder': u'Страна'}),
            'region': forms.TextInput(attrs={'placeholder': u'Регион'}),
            'city': forms.TextInput(attrs={'placeholder': u'Город'}),
            'address': forms.TextInput(attrs={'placeholder': u'Адрес'}),
        }