from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponse
import os

def index (request):

    return render(request, 'principal/index.html')
