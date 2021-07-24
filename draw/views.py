# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
})

def memo(request):
    return render(request, 'memo/index.html')

def memoboard(request):
    return render(request, 'memo/board.html')