from django import forms   
from .models import Comments

class TestovoeForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment','item_id']
    