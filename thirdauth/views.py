from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def home(request):
    context = RequestContext(request,
                            {'user': request.user,
                             'request': request})
    return render_to_response('thirdauth/home.html', context_instance=context)
