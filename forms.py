from django import forms
from .models import Enquiry
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name','phone','email','product_interest','location','message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Your full name','autocomplete':'name'}),
            'phone': forms.TextInput(attrs={'placeholder':'Phone / WhatsApp number','autocomplete':'tel'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email address (optional)','autocomplete':'email'}),
            'location': forms.TextInput(attrs={'placeholder':'City / district'}),
            'message': forms.Textarea(attrs={'placeholder':'Tell us what you need…','rows':4}),
        }
