from django import forms


class formContact(forms.Form):
    nameUser = forms.CharField(label='Your name', max_length=50, required=True)
    emailUser = forms.CharField(label='Your mail', required=True)
    descriptionUser = forms.CharField(
        label='Description', required=True, widget=forms.Textarea)
