from django import forms

class EmailForm(forms.Form):
    user_email = forms.CharField(label='Your email', max_length=100)

class APIForm(forms.Form):
    pass