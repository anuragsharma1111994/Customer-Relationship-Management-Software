from django import forms
from django.forms import fields
from .models import Lead
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent'
        )


class LeadForm(forms.Form):
    first_name = forms.CharField() 
    last_name = forms.CharField()
    age = forms.IntegerField()

class CustomUserCretionForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('username',)
        filed_classes = {'username':UsernameField}