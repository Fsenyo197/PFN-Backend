from django import forms
from tinymce.widgets import TinyMCE
from cloudinary.forms import CloudinaryFileField
from blog.models.discount_model import DiscountCode

class DiscountCodeCreateForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={
        'class': 'form-control',
        'id': 'discountBody',
        'name': 'discount_body',
    }))
    image = CloudinaryFileField(
        options={
            'class': 'form-control',
            'id': 'discountImage'
        },
        required=False  # Make image optional if desired
    )

    class Meta:
        model = DiscountCode
        fields = ['firm_name', 'discount_code', 'discount_percentage', 'image', 'title', 'body', 'date', 'duration']
        widgets = {
            'firm_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Firm Name',
                'id': 'firmName'
            }),
            'discount_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Discount Code',
                'id': 'discountCode'
            }),
            'discount_percentage': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Discount Percentage',
                'id': 'discountPercentage'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Title',
                'id': 'discountTitle'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'discountDate'
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Duration (in days)',
                'id': 'discountDuration'
            })
        }

class DiscountCodeUpdateForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={
        'class': 'form-control',
        'id': 'discountBody',
        'name': 'discount_body',
    }))
    image = CloudinaryFileField(
        options={
            'class': 'form-control',
            'id': 'discountImage'
        },
        required=False  # Make image optional if desired
    )

    class Meta:
        model = DiscountCode
        fields = ['firm_name', 'discount_code', 'discount_percentage', 'image', 'title', 'body', 'date', 'duration']
        widgets = {
            'firm_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Firm Name',
                'id': 'firmName'
            }),
            'discount_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Discount Code',
                'id': 'discountCode'
            }),
            'discount_percentage': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Discount Percentage',
                'id': 'discountPercentage'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Title',
                'id': 'discountTitle'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'discountDate'
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Duration (in days)',
                'id': 'discountDuration'
            })
        }
