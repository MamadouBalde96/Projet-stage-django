from django.shortcuts import render
from django.http import HttpResponseRedirect
from .formulaire import ListesForm
from django.views import View
from .formulaire import ListesForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from  django.template.loader import render_to_string

def student(request):
    if request.method == "POST":
        form=ListesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = request.POST['message']
            sujet = request.POST['sujet']
            courriel = request.POST['email']
            template = render_to_string('email_template.html', {'prenom': request.POST['prénom'], 'nom': request.POST['nom'], 'promotion': request.POST['niveau'] ,'dept': request.POST['département']})
            send_mail(sujet, message, courriel, ['votre e-mail de reception'], fail_silently=False)
            email = EmailMessage(
                sujet,
                template,
                settings.EMAIL_HOST_USER,
                [courriel],
            )
            email.fail_silently=False
            email.send()
            success = "message envoyé avec succès !"
            form = ListesForm()
        return render(request,"index.html",  {"success":success, "form":form})
    else:
        form=ListesForm()
        return render(request,"index.html", {"form":form})