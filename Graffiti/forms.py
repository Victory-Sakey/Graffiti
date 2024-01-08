from django import forms
from .models import ContactFormSubmission , JoinCommunitySubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormSubmission
        fields = ['name', 'email', 'message']

        widgets = {
            'message': forms.Textarea(attrs={'rows': 10, 'cols': 40 , 'name': 'message'}),  # Adjust rows and cols as needed
        }

class JoinCommunityForm(forms.ModelForm):
    class Meta:
        model = JoinCommunitySubmission
        fields = ['name', 'email', 'Phone_number']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2 text-gray-700 focus:outline-none', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border rounded px-3 py-2 text-gray-700 focus:outline-none', 'placeholder': 'Email'}),
            'Phone_number': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2 text-gray-700 focus:outline-none',   'placeholder': 'Phone Number'}),
        }

        
