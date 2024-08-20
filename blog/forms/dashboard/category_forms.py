from django import forms
from blog.models.category_model import Category
from ckeditor.widgets import CKEditorWidget

class CategoryCreateForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(config_name='default', attrs={
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
    description = forms.CharField(widget=CKEditorWidget(config_name='default', attrs={
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
