from django.shortcuts import render

def base_template(request):
    return render(request, 'base.html')
