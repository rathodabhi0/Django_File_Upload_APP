from django import forms

from .models import ls_20


class DocumentForm(forms.ModelForm):
    class Meta:
        model = ls_20
        fields = ('Elect_file',)