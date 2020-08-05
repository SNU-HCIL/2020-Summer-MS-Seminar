from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
@login_required
def index(request, squares):
    return JsonResponse({
        'next': playAI(squares)
    })

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