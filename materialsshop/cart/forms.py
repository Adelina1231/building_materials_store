from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    update = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput)
