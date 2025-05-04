from django.shortcuts import render,HttpResponse
from . import models
from .forms import ContactForm


# Create your views here.
def home(request):
  recipies = models.Recipies.objects.all()
  context = {
    'recipies': recipies
  }
  return render(request, "recipies/home.html", context)

def about(request):
  return render(request, "recipies/about.html")

def contact(request):
  form = ContactForm()
  if request.method == "POST":
    form = ContactForm(request.POST)
    form.save()

  context = {
    'ContactForm': form,
  }
  return render(request, "recipies/contact.html", context)


