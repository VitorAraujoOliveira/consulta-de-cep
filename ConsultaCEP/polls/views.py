from django.shortcuts import render

from django.http import HttpResponse



response  ='''
<html> {aaa} <html>

'''

def index(request):
    return HttpResponse(response)