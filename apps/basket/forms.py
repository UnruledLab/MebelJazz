#-*-coding:utf8-*-

from oscar.apps.basket.forms import *
from oscar.apps.basket.forms import AddToBasketForm as CoreAddToBasketForm

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils.html import escape, conditional_escape
from django.utils.encoding import force_unicode


class ImageChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return mark_safe("<img src='%s'/>" % obj.variant.image.url) \
            if obj.variant.image \
            else mark_safe('%s %s'%(obj.variant.name, obj.variant.group.postfix))


class AddToBasketForm(CoreAddToBasketForm):

    def __init__(self, basket, product, *args, **kwargs):
        super(AddToBasketForm, self).__init__(basket, product, *args, **kwargs)
        self._create_option_fields()

    def _create_option_fields(self):
        radio_num = 0
        select_num = 0
        for option in self.parent_product.multiple_options.all():
            choices = []

            if option.group.display_type == 'radio':
                widget = forms.RadioSelect(attrs={'class': 'option'})
                radio_num +=1
            else:
                widget = forms.Select(attrs={'class': 'option'})
                select_num +=1

            self.fields[option.group.code] = ImageChoiceField(
                widget=widget,
                queryset=option.choices.all(),
                label=option.group.name,
                required=option.is_required,
                empty_label=None
            )
        self.radio_num = radio_num
        self.select_num = select_num

    def cleaned_multiple_options(self):
        options = []
        data = self.cleaned_data
        for option in self.parent_product.multiple_options.all():
            if option.group.code in data and data[option.group.code] :
                options.append({
                    'multi_option': option,
                    'value': data[option.group.code]})

        return options

    def options_product_price(self, request):
        data = self.cleaned_multiple_options()
        add_price = sum([i['value'].additional_price
                         for i in data
                         if i['value'] and i['value'].additional_price]
                        )
        if self.product.is_parent:
            session = request.strategy.fetch_for_parent(self.product)
        else:
            session = request.strategy.fetch_for_product(self.product)

        base_price = session.price.incl_tax if  session.price.incl_tax else session.price.excl_tax
        if base_price:
            return base_price + add_price
        else:
            return 0


class SimpleAddToBasketForm(AddToBasketForm):
    quantity = forms.IntegerField(
        initial=1, min_value=1, widget=forms.HiddenInput, label=_('Quantity'))

