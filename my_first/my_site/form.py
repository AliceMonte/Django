from django import forms

class Form1(forms.Form):
    name = forms.CharField(label="Имя",max_length=45)