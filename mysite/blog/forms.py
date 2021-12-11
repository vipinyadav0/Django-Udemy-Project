from django import forms
from blog.models import Post, Comment

class PostForm(froms.ModelForm):


    class Meta():
        model = Post
        fields = ('author', 'title' 'text')

        widget = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}), # textarea is our own class//
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(froms.ModelFOrm):

    class Meta():
        model = Comment
        fields = ('auhtor','text')

        widget = {
            'author':forms.TextInput(attrs={'class':'textinputclass'})
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }