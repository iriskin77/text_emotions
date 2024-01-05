from django import forms
from .models import FileModel


class ProcessFileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ['author', 'name_column', 'file']

        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор документа'
            }),
            'name_column': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название колонки'
            }),

        }
