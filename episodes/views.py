from django.shortcuts import render

# Create your views here.
def show_home(request):
    return render(request, "episodes/home.html")

def show_about(request):

    return render(request, "episodes/about.html")

def show_contact(request):
    return render(request, "episodes/contact.html")
