from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
#CODIGO PARA EL FORMULARIO DE ENVIO DE CORREO (contact/views.py)
# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
       contact_form = ContactForm(data=request.POST)
       if contact_form.is_valid():
            name = request.POST.get('name')
            mail = request.POST.get('mail')
            content = contact_form.cleaned_data.get('content')

            #creamos el correo
            email_message = EmailMessage(
                "CarmenManjarres: Nuevo mensaje de contacto", #Asunto
                f"De {name} ({mail})\n\nEscribió:\n\n{content}",  # Cuerpo del mensaje
                settings.EMAIL_HOST_USER,
                ["operadorpersonal0@gmail.com"], #emaildedestino
                reply_to=[mail]
            )

            # lo enviamos y redireccionamos
            try:
               email_message.send()
               # Si el correo se envía correctamente, redirigir con parámetro 'ok'
               return redirect(reverse('contact')+"?ok")
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
                #Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
           
    return render(request, "contact/contact.html", {'form':contact_form})
