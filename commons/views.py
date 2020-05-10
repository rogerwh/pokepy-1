from django.shortcuts import render

from .tasks import websocket_example_task

def websocket_example(request):
    task = websocket_example_task.delay()
    facility = task.id
    return render(request, 'websocket_example.html', {'facility': facility})
