from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect


def index(request):
    context = {'user': request.user}
    if request.user and not request.user.is_anonymous():
        return redirect('/home')
    else:
        return TemplateResponse(request, 'thirdauth/login_form.html', context=context)


def home(request):
    if request.user and not request.user.is_anonymous():
        return TemplateResponse(request, 'thirdauth/home.html', context={})
    else:
        return redirect('/')
