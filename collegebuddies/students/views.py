from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return render(request, 'precolleges/index.html')

    return HttpResponse("*****************Welcome to College Buddies********************")
# Create your views here.
def about(request):
    context = {}
    return render(request, 'students/about.html', context)

#def main(request):
  #  context = {}
#    return render(request, 'preloans/main.html', context)
    
def contacts(request):
    context = {}
    return render(request, 'students/contacts.html', context)
    
def services(request):
    context = {}
    return render(request, 'students/services.html', context)
    