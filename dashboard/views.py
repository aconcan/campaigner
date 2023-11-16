from django.shortcuts import render, Http404

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:    
        return render(request, 'index.html', {})
    else:
        raise Http404()