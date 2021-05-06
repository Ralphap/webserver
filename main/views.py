from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import PlayerForm



# Create your views here.
def homepage(request):
  if request.method == "POST":
    form = PlayerForm(request.POST)
    if form.is_valid():
      


      userinput = form.cleaned_data['name']
      request.session['userinput'] = userinput
      return redirect(reverse('main:welcomes'))

  
  form = PlayerForm()
  return render(request, "home.html", {"form": form})
  
  






def welcomes(request):
  userinput = request.session['userinput']
  
  my_context = {
    "nameofuser": userinput 
  }
  

  return render(request,"welcome.html",my_context)
