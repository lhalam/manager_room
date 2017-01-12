from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from room.models import Room


def index(request):
    rooms = Room.objects.all()
    context = {
        'rooms' : rooms
    }

    return render(request, 'room/home.html' , context)

def show_room(requst, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(requst, 'room/room.html' , {'room': room})

def user(requst):
    users = User.objects.all()
    context = {
        'users' : users
    }

    return render(requst, 'user/user.html' , context)