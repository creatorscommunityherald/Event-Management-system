from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets

from .models import Registration


class Event_Registration(forms.ModelForm):
    """
    Responsible for handlng Event Registration form
    """
    class Meta:
        model = Registration
        fields = [
            'name','email','phonenumber'
        ]
        widgets ={
            'name': forms.TextInput(attrs={
                'placeholder':'Attendee Name',
                'class':'form-control',
                'style':"margin-top: 0px"
            }),
            'email': forms.TextInput(attrs={
               'placeholder':'Attendee Email',
               'class':'form-control',
               'style':"margin-top: 12px"
            }),
            'phonenumber':forms.TextInput(attrs={
                'placeholder':'phonenumber',
                'class':'form-control',
                'style':"margin-top: 12px"
            }) 
        }