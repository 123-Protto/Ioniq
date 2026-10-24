
import re
from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = [
            'name',
            'phone',
            'email',
            'product_interest',
            'location',
            'message',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your full name',
                'autocomplete': 'name',
            }),

            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter 10-digit phone number',
                'autocomplete': 'tel',
                'type': 'tel',
                'inputmode': 'numeric',
                'maxlength': '10',
                'minlength': '10',
                'pattern': '[0-9]{10}',
                'oninput': "this.value = this.value.replace(/\\D/g, '').slice(0, 10)",
                'title': 'Enter exactly 10 digits',
                'required': True,
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Email address (optional)',
                'autocomplete': 'email',
            }),

            'location': forms.TextInput(attrs={
                'placeholder': 'City / district',
            }),

            'message': forms.Textarea(attrs={
                'placeholder': 'Tell us what you need…',
                'rows': 4,
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        digits = re.sub(r'\D', '', phone)

        if not re.fullmatch(r'[0-9]{10}', digits):
            raise forms.ValidationError(
                'Please enter a valid 10-digit phone number.'
            )

        return digits
