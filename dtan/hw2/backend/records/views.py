from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.conf import settings
from http import HTTPStatus
# https://docs.python.org/3/library/http.html#http.HTTPStatus

from .models import Record

# Create your views here.
def auth(request):
    if request.method == 'GET':
        # logout
        if not request.user.is_authenticated:
            return HttpResponse("You haven't logged in.", status_code=HTTPStatus.FORBIDDEN)
        logout(request)
        return HttpResponse("Success to log out.", status_code=HTTPStatus.OK)
    if request.method == 'POST':
        # login
        if request.user.is_authenticated:
            return HttpResponse("You have already logged in.", status_code=HTTPStatus.FORBIDDEN)
        d = request.data
        try:
            username = d['username']
            password = d['password']
            user = authenticate(request, username, password)
            if user is not None:
                login(request, user)
                return HttpResponse('Success to log in.', status_code=HTTPStatus.OK)
            return HttpResponse('Invalid username or password.', status_code=HTTPStatus.FORBIDDEN)
        except KeyError:
            return HttpResponse('Bad request.', status_code=HTTPStatus.BAD_REQUEST)
    else:
        return HttpResponse('This method is not allowed.', status_code=HTTPStatus.METHOD_NOT_ALLOWED)

def records(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse("Not found.", status_code=HTTPStatus.NOT_FOUND)
        d = request.data
        record = None
        try:
            record = Record.objects.get(user__name==request.user.username)
        except Record.DoesNotExist:
            record = Record(user=request.user, win=0, draw=0, lose=0)
        try:
            if d['result'] == 'win':
                record.win += 1
            elif d['result'] == 'draw':
                record.draw += 1
            elif d['result'] == 'lose':
                record.lose += 1
            record.save()
            return JsonResponse(record.as_dict())
        except KeyError:
            return HttpResponse('Bad request.', status_code=HTTPStatus.BAD_REQUEST)
    else:
        return HttpResponse('This method is not allowed.', status_code=HTTPStatus.METHOD_NOT_ALLOWED)
    