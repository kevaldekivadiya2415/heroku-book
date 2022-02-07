from django import forms
from books.models import Review


class ReviewForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={
                           'class': "border rounded p-2 w-full", 'placeholder': "Write your review here"}))
    image = forms.ImageField(required=False)

    