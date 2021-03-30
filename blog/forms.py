from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    super(PostForm, self).__init__(*args, **kwargs)

    # self.fields['title'].max_length = '100'

  title = forms.CharField(
    widget=forms.TextInput(attrs={
      'maxlength': '100'
    })
  )

  class Meta:
    model = Post
    fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

  text = forms.CharField(
    label='Write a comment',
    widget=forms.Textarea(
      attrs={
        'class': 'border-2 border-rounded-lg border-gray-400 block resize-none w-full h-24 p-2 mt-4'
      }
    )
  )
  class Meta:
    model = Comment
    fields = ('text',)
