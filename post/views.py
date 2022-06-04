from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def home(request):
    return redirect('upload/')


def upload_recipes(request):
    if request.method == 'GET':
        form = RecipeForm()
        return render(request, 'upload.html', {'form':form})
    # elif request.method == 'POST':
        #form = RecipeForm(request.POST, reqeust.FILES)
        #if form.is valid()
