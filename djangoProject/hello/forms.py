from django import forms
from .models import contactinfo

class ContactForm(forms.ModelForm):
    class Meta:
        model = contactinfo
        fields = '__all__'