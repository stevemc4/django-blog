from django import forms
from blog.models import Post

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

