from django import forms
from .models import Donor

# Create forms

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = "__all__"

