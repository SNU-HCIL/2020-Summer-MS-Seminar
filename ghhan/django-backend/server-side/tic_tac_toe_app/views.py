from .playAI import playAI

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View

from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from django.utils.dateparse import parse_datetime
from .models import Game

@ensure_csrf_cookie
def index(request):
    return HttpResponse(status=200)

def logIn(request):
    if request.method == "POST":
        username = request.POST['userID']
        password = request.POST['password']
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                'was_successful': True,
                'message': "Log In Succeeded."
            })

        else:
            return JsonResponse({
                'was_successful': False,
                'message': "Log In Failed."
            })

def GameHistory(request):
    if request.method == "GET":
        user = User.objects.get(username=request.session.username)
        gamelogs = user.games.all()
        return JsonResponse({
            'game_logs':  [{'result': gamelog.result_text} for gamelog in gamelogs],
            'was_successful': True,
            'message': "Saved Game Logs For Current User"
        }) 
    else:
       return JsonResponse({
            'was_successful': False,
            'message': "Invalid Operation"
        }) 

def SaveGameResult(request):
    if request.method == "POST":
        user = User.objects.get(username=request.session.username)
        
        start = parse_datetime(request.POST['start'])
        result = request.POST['result']
        turns = request.POST['turns']

        gameResult = user.games.create(
            start_date=start,
            result_text=result,
            game_turns = turns
        )
        return JsonResponse({
            'was_successful': True,
            'message': "Saved a New Result" + str(gameResult)
        })
    else:
        return JsonResponse({
            'was_successful': False,
            'message': "Problems in Saving"
        })

def RetrieveAIAction(request):
    if request.method == "POST":
        received = request.POST['game_status']
        return JsonResponse({
            'was_successful': True,
            'next_action': playAI(received) ,
            'message': "Problems in Saving"
        })
    else: 
        return JsonResponse({
            'was_successful': False,
            'message': "Problem Occured During Transaction."
        })


def logOut(request):
    logout(request)
    return JsonResponse({
        'was_successful': True,
        'message': "Log Out Succeeded."
    })




