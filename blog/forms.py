from .models import Comment
from django import forms

#Comment Form Content
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

#Contact Form İnformation
class ContactForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)