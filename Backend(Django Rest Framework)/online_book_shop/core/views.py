
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

#from django.views.decorators.csrf import csrf_exempt

# Step 1 :
# Create your views here.
# def apage(request):
#     return JsonResponse({"Username":"Aakash",
#                          "Email":"savantaakash322@gmail.com"})



# you can get users from django admin panel 

from django.contrib.auth.models import User


# @csrf_exempt
# def apage(request):
    
#     user: User = User.objects.get(pk=1)
    
    
    
    
    
    
#     return JsonResponse({"Username":user.username,
#                          "Email":user.email})





#@csrf_exempt
def apage(request):
    
    user: User = User.objects.get(pk=1)
    
    username = request.POST.get("username")
    email = request.POST.get("email")
    print(username)
    print(email)
    
    return JsonResponse({"Username":user.username,
                         "Email":user.email})


