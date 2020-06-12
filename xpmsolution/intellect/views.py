from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect





def home(request):
    template_name = 'intellect/index.html'
    return render(request, template_name)