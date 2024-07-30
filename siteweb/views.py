from django.shortcuts import render, redirect, get_object_or_404
from siteweb.models import Project, Language, Skill, Resume, Education, Experience, Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def home(request):
    return  render(request, "siteweb/index.html")


def projet(request):
    projects = Project.objects.all()

    return render(request, 'siteweb/projet.html', context={"projects": projects})


def education(request):
    educations = Education.objects.all()

    return render(request, 'siteweb/cv.html', context= {"educations": educations})


def experience(request):
    experiences = Experience.objects.all()

    return render(request, 'siteweb/cv.html', context= {"experiences": experiences})


def skill(request):
    skills = Skill.objects.all()

    return render(request, 'siteweb/cv.html', context= {"skills": skills})


def language(request):
    languages = Language.objects.all()

    return render(request, 'siteweb/cv.html', context= {"languages": languages})


# def cv_detail(request, pk):
#     resumes = get_object_or_404(Resume, pk=pk)
#     context = {
#         'resumes': resumes,
#         'educations': resumes.educations.all(),
#         'experiences': resumes.experiences.all(),
#         'skills': resumes.skills.all(),
#         'languages': resumes.languages.all(),
#     }
#
#     return render(request, 'siteweb/cv_detail.html', context)


def cv(request):
    resumes = Resume.objects.all()
    languages = Language.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()

    context = {
        'resumes': resumes,
        'educations': educations,
        'experiences': experiences,
        'skills': skills,
        'languages': languages
    }
    return render(request, 'siteweb/cv.html', context)


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

    # # Envoyer un email de confirmation
    # send_mail(
    #     f'New contact form submission from {name} {lastname}: {object}', message,
    #     settings.DEFAULT_FROM_EMAIL,
    #     [settings.CONTACT_EMAIL],
    #     fail_silently=False,
    # )

    return render(request, 'siteweb/contact.html')