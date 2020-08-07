from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Task
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def index(request):
    return HttpResponse(status=200)

class Tasks(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return JsonResponse({
            'tasks': [
                {
                    'title': task.title,
                    'completed': task.completed
                }
                for task in tasks
            ]
        })

    def post(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return JsonResponse({
            'message': 'You succeeded to request POST!',
            'tasks': [
                {
                    'title': task.title,
                    'completed': task.completed
                }
                for task in tasks
            ]
        })




