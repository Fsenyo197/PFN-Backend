from django import forms
from django.forms import TextInput, Select, FileInput
from django_summernote.widgets import SummernoteWidget
from blog.models.article_model import Article
from blog.models.category_model import Category


class ArticleCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(approved=True),
        empty_label="Select Category",
        widget=forms.Select(
            attrs={
                "class": "form-control selectpicker",
                "data-live-search": "true",
            }
        ),
    )

    class Meta:
        model = Article
        fields = [
            "title", "category", "image", "image_url", "image_credit",
            "body", "tags", "status"
        ]
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
            }),
            'image': FileInput(attrs={
                "class": "form-control clearablefileinput",
            }),
            'image_url': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Paste Cloudinary image URL here",
            }),
            'image_credit': TextInput(attrs={
                'class': "form-control",
            }),
            'body': SummernoteWidget(attrs={  # Use SummernoteWidget
                'summernote': {
                    'width': '100%',
                    'height': '400',
                },
            }),
            'tags': TextInput(attrs={
                'class': "form-control",
                'data-role': "tagsinput",
            }),
            'status': Select(choices=Article.STATUS_CHOICES, attrs={
                "class": "form-control selectpicker",
                "data-live-search": "true",
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        image_url = cleaned_data.get('image_url')

        # Validate that only one of `image` or `image_url` is provided
        if image and image_url:
            raise forms.ValidationError("Provide either an uploaded image or a Cloudinary image link, not both.")
        if not image and not image_url:
            raise forms.ValidationError("You must provide either an uploaded image or a Cloudinary image link.")

        return cleaned_data


class ArticleUpdateForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(approved=True),
        empty_label="Select Category",
        widget=forms.Select(
            attrs={
                "class": "form-control selectpicker",
                "type": "text",
                "name": "article-category",
                "id": "articleCategory",
                "data-live-search": "true"
            }
        )
    )

    class Meta:
        model = Article
        fields = ["title", "category", "image", "image_credit", "body", "tags", "status"]
        widgets = {
            'title': TextInput(attrs={
                'name': "article-title",
                'class': "form-control",
                'id': "articleTitle"
            }),
            'image_credit': TextInput(attrs={
                'name': "image_credit",
                'class': "form-control",
                'id': "image_credit"
            }),
            'status': Select(choices=Article.STATUS_CHOICES, attrs={
                "class": "form-control selectpicker",
                "name": "status", "type": "text",
                "id": "articleStatus",
                "data-live-search": "true",
                "title": "Select Status"
            }),
            'body': SummernoteWidget(attrs={  # Use SummernoteWidget
                'summernote': {
                    'width': '100%',
                    'height': '400',
                },
            }),
            'image': FileInput(attrs={
                "class": "form-control clearablefileinput",
                "type": "file",
                "id": "articleImage",
                "name": "article-image",
            }),
        }
