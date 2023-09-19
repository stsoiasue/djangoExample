from django import forms
from hello.models import LogMessage, Rating

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",) # NOTE: the trailing comma is required

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ("rating",) # NOTE: the trailing comma is required