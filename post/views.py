from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse

# Create your views here.

def home(request):
    return redirect('upload/')


def upload_recipes(request):
    if request.method == 'GET':
        form = RecipeForm()
        return render(request, 'upload.html', {'form':form})
    elif request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            return HttpResponse('fail')

