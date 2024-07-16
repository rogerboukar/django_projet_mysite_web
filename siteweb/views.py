from django.shortcuts import render
# Create your views here.

def home(request):
    return  render(request, "siteweb/index.html")


def cv(request):
    return render(request, 'siteweb/cv.html')

def projet(request):
    return render(request, 'siteweb/projet.html')

def contact(request):
    return render(request, 'siteweb/contact.html')