from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from .forms import EmailForm
def sign_up(request,form):
    headers = {}
    url = 'https://aqs.epa.gov/data/api/signup?email='+form.user_email
    r = request.get(url)
    return HttpResponseRedirect('/map/APIForm/')