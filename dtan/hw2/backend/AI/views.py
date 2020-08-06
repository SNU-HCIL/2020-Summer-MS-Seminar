from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from http import HTTPStatus
import random

# Create your views here.
@ensure_csrf_cookie
def index(request):
    if not request.user.is_authenticated:
        return HttpResponse("Not found.", status=HTTPStatus.NOT_FOUND)

    if request.method == 'POST':
        if request.META['CONTENT_TYPE'].find("application/json") != -1:
            d = json.loads(request.body)
        else:
            d = request.POST
        try:
            squares = d['squares']
            return JsonResponse({
                'next': playAI(d['squares'])
            })
        except KeyError:
            return HttpResponse('Bad request.', status=HTTPStatus.BAD_REQUEST)
    else:
        return HttpResponse('This method is not allowed.', status=HTTPStatus.METHOD_NOT_ALLOWED)


def playAI(squares):
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    candidates = []
    empty_squares = [i for i in range(len(squares)) if squares[i] is None]
    for i in range(len(lines)):
        [a, b, c] = lines[i]
        # Win
        if squares[a] is None and squares[b] is not None and squares[b] == squares[c]:
            if squares[b] == 'O':
                return a
            else :
                candidates.append(a)
        elif squares[b] is None and squares[c] is not None and squares[c] == squares[a]:
            if squares[c] == 'O':
                return b
            else:
                candidates.append(b)
        elif squares[c] is None and squares[a] is not None and squares[a] == squares[b]:
            if squares[a] == 'O':
                return c
            else:
                candidates.append(c)
    
    # Block
    if candidates:
        return candidates[random.randrange(0, len(candidates))]
    
    # Random
    else :
        return empty_squares[random.randrange(0, len(empty_squares))]