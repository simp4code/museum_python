# forms.py
from django import forms
from .models import ImportFile

class FileForm(forms.ModelForm):
    class Meta:
        model = ImportFile
        fields = ['file_image', 'file_name', 'file_abstract', 'file_pdf']
        widgets = {
            'file_image': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
            'file_name': forms.TextInput(attrs={'class': 'custom-text-input'}),
            'file_abstract': forms.Textarea(attrs={'class': 'custom-textarea'}),
            'file_pdf': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        }