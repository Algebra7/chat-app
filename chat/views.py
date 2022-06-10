from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.db.models.base import ObjectDoesNotExist

from chat.models import Room


@login_required
def chat_room(request, room_id):
    try:
        # check if rooom exist
        room = Room.objects.get(pk=room_id)
    except ObjectDoesNotExist:
        # room does not exist
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {"room": room})
