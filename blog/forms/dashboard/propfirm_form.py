from django import forms
from blog.models.propfirm_model import PropFirm

class PropFirmForm(forms.ModelForm):
    class Meta:
        model = PropFirm
        fields = '__all__'

    trading_platforms = forms.MultipleChoiceField(
        choices=PropFirm.TRADING_PLATFORMS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )