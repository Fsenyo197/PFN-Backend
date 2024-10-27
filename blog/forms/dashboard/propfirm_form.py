from django import forms
from blog.models.propfirm_model import PropFirm

class PropFirmForm(forms.ModelForm):
    class Meta:
        model = PropFirm
        fields = '__all__'  # Include all fields, or specify the fields you want

    trading_platforms = forms.MultipleChoiceField(
        choices=PropFirm.TRADING_PLATFORMS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    status = forms.ChoiceField(
        choices=PropFirm.STATUS_CHOICES,
        widget=forms.Select(attrs={
            "class": "form-control selectpicker",
            "name": "status",
            "id": "propFirmStatus",
            "data-live-search": "true",
            "title": "Select Status"
        }),
        required=True,
    )
