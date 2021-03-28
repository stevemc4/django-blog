from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):

  # def __init__(self, *args, **kwargs):
  #   super(PostForm, self).__init__(*args, **kwargs)

  #   for field in self.visible_fields():
  #     field.widget.attrs = {'class': 'border-2 border-gray-500'}

  class Meta:
    model = Post
    fields = ('title', 'text',)

