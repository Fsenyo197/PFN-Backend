from django import forms
from tinymce.widgets import TinyMCE
from blog.models.category_model import Category


class CategoryCreateForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={
        'class': 'form-control',
        'id': 'categoryDescription',
        'name': 'category_description',
    }))
    
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Category Name',
                'id': 'categoryName'
            })
        }


class CategoryUpdateForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={
        'class': 'form-control',
        'id': 'categoryDescription',
        'name': 'category_description',
    }))
    
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Category Name',
                'id': 'categoryName'
            })
        }
