from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse

# Create your views here.

def home(request):
    return redirect('upload/')


def upload_recipes(request):
    if request.method == 'GET':
        # form = RecipeForm()
        timecate = Timecate.objects.all()
        diffcate = Diffcate.objects.all()
        return render(request, 'upload.html', {'timecost':timecate, 'difficulty':diffcate})
    elif request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        # timecost = request.POST.get('timecost', '')
        # difficulty = request.POST.get('difficulty', '')

        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            return HttpResponse('fail')

