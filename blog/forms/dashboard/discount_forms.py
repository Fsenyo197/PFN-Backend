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
        required=False
    )
    image_credit = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'imageCredit',
    }))
    status = forms.ChoiceField(choices=DiscountCode.STATUS_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'discountStatus'
    }))

    class Meta:
        model = DiscountCode
        fields = ['firm_name', 'discount_code', 'discount_percentage', 'image', 'image_credit', 'title', 'body', 'date', 'duration', 'status',]
        widgets = {
            'firm_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'firmName'
            }),
            'discount_code': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'discountCode'
            }),
            'discount_percentage': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'discountPercentage'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'discountTitle'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'discountDate'
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
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
        required=False
    )
    image_credit = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'imageCredit',
    }))
    status = forms.ChoiceField(choices=DiscountCode.STATUS_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'discountStatus'
    }))

    class Meta:
        model = DiscountCode
        fields = ['firm_name', 'discount_code', 'discount_percentage', 'image', 'image_credit', 'title', 'body', 'date', 'duration', 'status',]
        widgets = {
            'firm_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'firmName'
            }),
            'discount_code': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'discountCode'
            }),
            'discount_percentage': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'discountPercentage'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'discountTitle'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'discountDate'
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'discountDuration'
            })
        }
