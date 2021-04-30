from django import forms
from django.forms.fields import CharField, IntegerField

# 2:50:19

class LeadForm(forms.Form):
    first_name = CharField() 
    last_name = CharField()
    age = IntegerField()