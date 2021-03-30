from django import forms
from blog.models import Post, Comment, Tag

class PostForm(forms.ModelForm):


  title = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'maxlength': '100',
        'class': 'border-2 rounded border-gray-400 block mt-2 mb-4 w-full p-2'
      })
  )

  text = forms.CharField(
    widget=forms.Textarea(
      attrs={
        'class': 'border-2 rounded border-gray-400 block mt-2 resize-x-none w-full p-2 mb-4'
      }
    )
  )

  tags = forms.ModelMultipleChoiceField(
    Tag.objects.all(),
    widget=forms.SelectMultiple(
      attrs={
        'class': 'border-2 rounded border-gray-400 block mt-2 mb-4 w-full p-2'
      }
    )
  )

  class Meta:
    model = Post
    fields = ('title', 'text', 'tags',)

class CommentForm(forms.ModelForm):

  text = forms.CharField(
    label='Write a comment',
    widget=forms.Textarea(
      attrs={
        'class': 'border-2 rounded border-gray-400 block resize-none w-full h-24 p-2 mt-4'
      }
    )
  )
  class Meta:
    model = Comment
    fields = ('text',)
