from django.shortcuts import render, redirect
from siteweb.models import Project
from siteweb.models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def home(request):
    return  render(request, "siteweb/index.html")


def cv(request):
    return render(request, 'siteweb/cv.html')

def projet(request):
    projects = Project.objects.all()

    return render(request, 'siteweb/projet.html', context={"projects": projects})


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         lastname = request.POST.get('lastname')
#         email = request.POST.get('email')
#         object = request.POST.get('object')
#         message = request.POST.get('message')
#
#         # Enregistrement des données dans la base de données
#
#         submission = Contact(name=name, lastname=lastname, email=email, object=object, message=message)
#         submission.save()
#
#         return render(request, 'siteweb/sucess.html')

        ## Envoyer un email de confirmation
        # send_mail(
        #     f'New contact form submission from {name} {lastname}: {object}',
        #     message,
        #     settings.DEFAULT_FROM_EMAIL,
        #     [settings.CONTACT_EMAIL],
        #     fail_silently=False,
        # )
    # else:
    #     return render(request, 'siteweb/contact.html')

def contact(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "Vous devez d'abord vous inscrire pour soumettre le formulaire.")
            return redirect('contact')  # Redirige l'utilisateur vers la page de contact

        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        object = request.POST.get('object')
        message = request.POST.get('message')

        # Enregistrement des données dans la base de données
        submission = Contact(name=name, lastname=lastname, email=email, object=object, message=message)
        submission.save()

        messages.success(request, "Votre message a été envoyé avec succès.")
        return render(request, 'siteweb/success.html')

    return render(request, 'siteweb/contact.html')