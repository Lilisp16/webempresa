from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Nombre'}
    ))

    mail = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Correo electronico'}
    ))

    content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'placeholder':'Escribe tu comentario'}
    ))
   