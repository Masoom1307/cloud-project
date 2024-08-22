from django import forms
from .models import Module

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'code', 'credit', 'category', 'description', 'availability', 'allowed_courses']
