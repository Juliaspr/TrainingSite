from django import forms
from .models import *


class EnrollForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['FIO', 'Trainer', 'Goals']


class EnrollGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['Probability']

