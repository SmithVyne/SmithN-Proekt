from django.shortcuts import render
from django.http import HttpResponse



def main_page(request):
    return render(request, 'main\Main.html')

def research_page(request):
    return render(request, 'main\Research.html')
