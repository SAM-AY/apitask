from django import forms
from .models import LinkApp

class LinkAppForm(forms.ModelForm):
    class Meta:
        model = LinkApp
        fields = [
            'target_url'
            'description'
            'identifier'
            'author'
            'created_date'
            'active'

        ]