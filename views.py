from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('example.view_example')
def index(request):
    context = {
        "text": "Hello world"
    }
    return render(request, 'example/index.html', context=context)