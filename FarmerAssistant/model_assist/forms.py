from django import forms
from model_assist.models import SubmittedImage

class SubmittedImageForm(forms.ModelForm):
    class Meta:
        model = SubmittedImage
