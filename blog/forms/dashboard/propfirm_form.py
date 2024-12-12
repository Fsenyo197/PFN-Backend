from django import forms
from blog.models.propfirm_model import PropFirm

class PropFirmForm(forms.ModelForm):
    class Meta:
        model = PropFirm
        fields = '__all__'

    # Define the trading platforms field
    trading_platforms = forms.MultipleChoiceField(
        choices=PropFirm.TRADING_PLATFORMS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    # Define the payment options field
    payment_options = forms.MultipleChoiceField(
        choices=PropFirm.PAYMENT_OPTIONS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    # Define the payout options field
    payout_options = forms.MultipleChoiceField(
        choices=PropFirm.PAYOUT_OPTIONS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
