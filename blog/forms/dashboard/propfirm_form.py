from django import forms
from blog.models.propfirm_model import PropFirm

class AccountPlanForm(forms.Form):
    account_size = forms.IntegerField(label='Account Size', required=False)
    price = forms.DecimalField(label='Price', required=False)
    daily_drawdown = forms.DecimalField(label='Daily Drawdown', required=False)
    total_drawdown = forms.DecimalField(label='Total Drawdown', required=False)

class PropFirmForm(forms.ModelForm):
    class Meta:
        model = PropFirm
        fields = '__all__'  # Use all fields or specify them as needed

    trading_platforms = forms.MultipleChoiceField(
        choices=PropFirm.TRADING_PLATFORMS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    phase_type = forms.MultipleChoiceField(
        choices=PropFirm.PHASE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    # This will hold the account plans; you can use a formset later to display it
    account_plans = forms.CharField(widget=forms.HiddenInput(), required=False)

    def clean(self):
        cleaned_data = super().clean()
        # Add any necessary validation logic here
