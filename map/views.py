from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from .forms import EmailForm
import services
# Create your views here.


def index(request):
    if request == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            services.sign_up(request,form)
    else:
        form = EmailForm()

    return render(request,'index.htm', {form: form})
def APIForm(request):
    pass
