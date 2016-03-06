from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.response import TemplateResponse


def home(request):
    context = RequestContext(request,
                             {'user': request.user,
                              'request': request})
    return render_to_response('thirdauth/login_form.html', context_instance=context)


def logged_in(request):
    context = {}
    return TemplateResponse(request, 'thirdauth/login_form.html', context={})