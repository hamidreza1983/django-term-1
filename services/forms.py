from django import forms
from .models import Comments



class CommnetsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["service", "name", "message"]