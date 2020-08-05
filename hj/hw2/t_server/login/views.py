from django.shortcuts import render

# Create your views here.

## For User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth

## For CSRF
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import tttUser
import json



@ensure_csrf_cookie
def index(request):
    return HttpResponse(status=200)

def signUp(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        users = tttUser.objects.filter(userId=body["id"])
        if users.__len__() > 0:
            return HttpResponse("Already existing ID")
        
        tttUser(userId=body["id"], win=0, lose=0, draw=0).save()
        return HttpResponse("Hello!! " + body["id"])
    
def signIn(request):
    if request.method == "PUT":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            user = tttUser.objects.get(userId=body["id"])
        except tttUser.DoesNotExist:
            return JsonResponse({
                'result': False
            })

        return JsonResponse({
            'result': True
        })
        
def status(request, user_id):
    if request.method == "GET":
        try:
            user = tttUser.objects.get(userId=user_id)
        except tttUser.DoesNotExist:
            return JsonResponse({
                'result': False
            })
        
        return JsonResponse({
            'result': True,
            'win': user.win,
            'draw': user.draw,
            "lose": user.lose,
        })

def gameResult(request):
    if request.method == "PUT":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            user = tttUser.objects.get(userId=body["id"])
        except tttUser.DoesNotExist:
            return JsonResponse({
                'result': False
            })

        if body["gameResult"] == "win":
            user.win += 1
        elif body["gameResult"] == "lose":
            user.lose += 1
        else:
            user.draw += 1
        
        user.save();
        return JsonResponse({
            'result': True,
            'win': user.win,
            'draw': user.draw,
            'lose': user.lose
        })
        