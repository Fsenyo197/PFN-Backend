from django import forms
from django.forms import TextInput, Select, FileInput
from tinymce.widgets import TinyMCE 

from blog.models.article_model import Article
from blog.models.category_model import Category


class ArticleCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(
                                      approved=True),
                                      empty_label="Select Category",
                                      widget=forms.Select(attrs=
                                                          {
                                                              "class": "form-control selectpicker",
                                                              "type": "text",
                                                              "name": "article-category",
                                                              "id": "articleCategory",
                                                              "data-live-search": "true"
                                                          }
                                      )
                                    )

    class Meta:
        # Article status constants
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # CHOICES
        STATUS_CHOICES = (
            (DRAFTED, 'Draft'),
            (PUBLISHED, 'Publish'),
        )

        model = Article
        fields = ["title", "category", "image", "image_credit", "body", "tags", "status"]
        widgets = {
            'title': TextInput(attrs={
                                     'name': "article-title",
                                     'class': "form-control",
                                     'id': "articleTitle"
                                     }),

            'image': FileInput(attrs={
                                        "class": "form-control clearablefileinput",
                                        "type": "file",
                                        "id": "articleImage",
                                        "name": "article-image"
                                      }

                               ),

            'image_credit': TextInput(attrs={
                'name': "image_credit",
                'class': "form-control",
                'id': "image_credit"
            }),

            'body': forms.CharField(widget=TinyMCE(attrs={
                       "rows": 5, "cols": 20,
                       'id': 'content',
                       'name': "article_content",
                       'class': "form-control",
                       })),

            'tags': TextInput(attrs={
                                     'name': "tags",
                                     'class': "form-control",
                                     'id': "tags",
                                     'data-role': "tagsinput"
                                     }),

            'status': Select(choices=STATUS_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "status", "type": "text",
                                 "id": "articleStatus",
                                 "data-live-search": "true",
                                 "title": "Select Status"
                             }
                             ),
        }


class ArticleUpdateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(
                                      approved=True),
                                      empty_label="Select Category",
                                      widget=forms.Select(attrs=
                                                          {
                                                              "class": "form-control selectpicker",
                                                              "type": "text",
                                                              "name": "article-category",
                                                              "id": "articleCategory",
                                                              "data-live-search": "true"
                                                          }
                                      )
                                    )

    class Meta:
        # Article status constants
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # CHOICES
        STATUS_CHOICES = (
            (DRAFTED, 'Draft'),
            (PUBLISHED, 'Publish'),
        )

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

            'status': Select(choices=STATUS_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "status", "type": "text",
                                 "id": "articleStatus",
                                 "data-live-search": "true",
                                 "title": "Select Status"
                             }
                             ),
            'body': forms.CharField(widget=TinyMCE(attrs={
                       "rows": 5, "cols": 20,
                       'id': 'content',
                       'name': "article_content",
                       'class': "form-control",
                       })),

            'image': FileInput(attrs={
                "class": "form-control clearablefileinput",
                "type": "file",
                "id": "articleImage",
                "name": "article-image",
            }

            ),
        }
