from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import NameForm


# localhost 127.0.0.1:8000 is searched in the browser, thus a http request is sent to the webserver

# This TCP connection/http request is handle by Django middleware found in setting.py, a level of abstraction in request response cycle. The equivalent 

# would be using modules http.server and socketserver, where the socketserver.tcpserver method would process tcp connection/http request and http.server 

# would serve the request files/html etc

# Once middleware handle Http request, pass it to the url router in mysite/mysite, where this line [path('', include('main.urls'))] will route

#to the url router in main app mysite/main/urls.py. From here it will extract url from request and match it to the define urls.

#http://127.0.0.1:8000 will default to homepage url. This causes the correspnding view function in views.py to be called.


def homepage(request):
  if request.method == "POST":
    form = NameForm(request.POST)
    if form.is_valid():
      


      userinput = form.cleaned_data['name']
      request.session['userinput'] = userinput
      return redirect(reverse('main:welcomes'))

  
  form = NameForm()
  return render(request, "home.html", {"form": form})

  
  
  #once the homepage function is called, function render returns html from templates/home.html in 

  #the Http response, the render function also accesses the form model (imported from forms.py) via context argument

  #so the schema for the form model is added to homepage html. 
  
  #the If statement comes  into affect if a name is submitted in the form, which get sent to webserver as http post request

  #second If statement checks if this the value submitted is 
  
  # valid e.g user click submit, sends http post request with no name in form, in that case conditional would fail
  
  #once both have passed form.cleaned_data method extract name out of the form data 

  #request.session method allows me to store the name value and use it in the  welcomes view function

  #return redirect(reverse('main:welcomes')) redirects user from homepage to welcomes page, it does this by reserve resolve to find url 

  #this results in welcomes view function being called.





def welcomes(request):
  userinput = request.session['userinput']
  

  return render(request,"welcome.html",{ "nameofuser": userinput })




#userinput is accessible by request.session method from homepage view 

#The userinput is put in dictionary

#return render serve http response with welcomes.html template. The dictionary is also passed as argument  

# resulting in name value being added to template html

# results in the hello with name response seen in browser. h2>Hello  {{nameofuser}}</h2