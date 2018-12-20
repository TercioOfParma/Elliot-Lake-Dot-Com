from django import forms


class bookForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100000)
    imagename = forms.CharField(max_length=100)

