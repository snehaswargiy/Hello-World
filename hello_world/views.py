from django.shortcuts import render, HttpResponse

# Create your views here.
def show(request):
    return HttpResponse('Hello World !This is <b>Sneha Sharad Swargiy</b> of <b>T4 batch</b> and my <b>PRN 1942208</b>')