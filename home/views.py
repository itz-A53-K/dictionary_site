from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
import requests

# Create your views here.
def home(request):
    if request.method == 'POST':
        srcInp= request.POST.get("word")
        apiResponse=requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+srcInp).json()

        return JsonResponse({"success": True, "apiResp": apiResponse})
    else:
        pass
    
    return render(request,'home/home.html')

