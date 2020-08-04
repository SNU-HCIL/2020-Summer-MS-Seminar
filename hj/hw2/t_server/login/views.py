from django.shortcuts import render

# Create your views here.

## For User
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

## For CSRF
from django.views.decorators.csrf import ensure_csrf_cookie
import json

@ensure_csrf_cookie
def index(request):
    return HttpResponse(status=200)

def signUp(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        return HttpResponse("Hello!! " + body["id"])