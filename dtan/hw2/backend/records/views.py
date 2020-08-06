from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import json
from http import HTTPStatus
# https://docs.python.org/3/library/http.html#http.HTTPStatus

from .models import Record

# Create your views here.
@ensure_csrf_cookie
def auth(request):
    if request.method == 'GET':
        # logout
        if not request.user.is_authenticated:
            return HttpResponse("You haven't logged in.", status=HTTPStatus.FORBIDDEN)
        logout(request)
        return HttpResponse("Success to log out.", status=HTTPStatus.OK)
    if request.method == 'POST':
        # login
        if request.user.is_authenticated:
            return HttpResponse("You have already logged in.", status=HTTPStatus.FORBIDDEN)
        if request.META['CONTENT_TYPE'].find("application/json") != -1:
            d = json.loads(request.body)
        else:
            d = request.POST
        try:
            username = d['username']
            password = d['password']
            if username is None or password is None:
                return HttpResponse('Bad request.', status=HTTPStatus.BAD_REQUEST)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Success to log in.', status=HTTPStatus.OK)
            return HttpResponse('Invalid username or password.', status=HTTPStatus.FORBIDDEN)
        except KeyError:
            return HttpResponse('Bad request.', status=HTTPStatus.BAD_REQUEST)
    else:
        if not request.user.is_authenticated:
            return HttpResponse("Not found.", status=HTTPStatus.NOT_FOUND)
        return HttpResponse('This method is not allowed.', status=HTTPStatus.METHOD_NOT_ALLOWED)

@ensure_csrf_cookie
def records(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return HttpResponse("Not found.", status=HTTPStatus.NOT_FOUND)
        try:
            record = Record.objects.get(user=request.user.username)
        except Record.DoesNotExist:
            record = Record(user=request.user.username, win=0, draw=0, lose=0)
            record.save()
        return JsonResponse(record.as_dict())

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse("Not found.", status=HTTPStatus.NOT_FOUND)
        if request.META['CONTENT_TYPE'].find("application/json") != -1:
            d = json.loads(request.body)
        else:
            d = request.POST
        record = None
        try:
            record = Record.objects.get(user=request.user.username)
        except Record.DoesNotExist:
            record = Record(user=request.user.username, win=0, draw=0, lose=0)
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
            return HttpResponse('Bad request.', status=HTTPStatus.BAD_REQUEST)
    else:
        if not request.user.is_authenticated:
            return HttpResponse("Not found.", status=HTTPStatus.NOT_FOUND)
        return HttpResponse('This method is not allowed.', status=HTTPStatus.METHOD_NOT_ALLOWED)

@ensure_csrf_cookie
def index(request):
    if request.method == 'GET':
        # check if user logged in
        if not request.user.is_authenticated:
            return HttpResponse("You haven't logged in.", status=HTTPStatus.FORBIDDEN)
        else:
            return HttpResponse("You have already logged in.", status=HTTPStatus.OK)
    else:
        if not request.user.is_authenticated:
            return HttpResponse("Not found.", status=HTTPStatus.NOT_FOUND)
        return HttpResponse('This method is not allowed.', status=HTTPStatus.METHOD_NOT_ALLOWED)

@ensure_csrf_cookie
def hello(request):
    response = HttpResponse(status=HTTPStatus.OK)
    # response.set_cookie('cookie', '', samesite='None')
    return response