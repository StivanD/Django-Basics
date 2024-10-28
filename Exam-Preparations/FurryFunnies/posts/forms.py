from django import forms
from django.forms import TextInput, Textarea

from FurryFunnies.mixins import ReadOnlyMixin
from posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': TextInput(
                attrs={
                    'placeholder': 'Put an attractive and unique title...'
                }
            ),
            'content': Textarea(
                attrs={
                    'placeholder': 'Share some interesting facts about your adorable pets...'
                }
            )
        }

        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content'
        }


class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['title', 'image_url', 'content']


class PostEditForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['title', 'image_url', 'content']
        help_texts = {
            'image_url': ''
        }


class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['title', 'image_url', 'content']
        help_texts = {
            'image_url': ''
        }
