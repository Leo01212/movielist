from django import forms
from .models import movie_details

class updat(forms.ModelForm):
    class Meta:
        model=movie_details
        fields=['year','im']