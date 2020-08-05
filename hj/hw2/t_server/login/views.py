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


import random

def playAI(squares) :
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];


    candidates = []
    empty_squares = [i for i in range(len(squares)) if squares[i] is None]

    for i in range(len(lines)) :
        [a, b, c] = lines[i]
        # Win
        if squares[a] is None and squares[b] is not None and squares[b] == squares[c] :
            if squares[b] == 'O' :
                return a
            else :
                candidates.append(a)
        elif squares[b] is None and squares[c] is not None and squares[c] == squares[a] :
            if squares[c] == 'O' :
                return b
            else:
                candidates.append(b)
        elif squares[c] is None and squares[a] is not None and squares[a] == squares[b] :
            if squares[a] == 'O' :
                return c
            else:
                candidates.append(c)
    
    # Block
    if candidates:
        return candidates[random.randrange(0, len(candidates))]
    
    # Random
    else :
        return empty_squares[random.randrange(0, len(empty_squares))]



# if __name__ == "__main__":
#     print(play([None, None, None, None, 'X', None, None, None, None ]))
#     print(play(['X', None, None, None, 'X', 'O', None, None, None ]))



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
        
def aiTurn(request, input):
    if request.method == "GET":
        input_list = list(input)
        input_final = [x if x is not "N" else None for x in input_list]
        return HttpResponse(int(playAI(input_final)))
    
        