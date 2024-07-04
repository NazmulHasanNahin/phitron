from django import forms
from album_model.models import *

class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields="__all__"
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
        