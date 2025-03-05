from django.shortcuts import render
#from cafe.views import index,coffee (應放在urls.py)
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def coffee(request):
    return render(request,"coffee/coffee.html")
def slogan(request) :
   return HttpResponse('''在忙也要隌你喝杯咖啡!!<br>
                        <a href='/coffee'>咖啡源起</a><br>
                         <a href='/'>首頁</a>
                       ''')