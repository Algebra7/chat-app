from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from chat.models import Room


@login_required
def chat_room(request, room_id):
    try:
        # check if rooom exist
        room = Room.objects.get(pk=room_id)
        # course = request.user.courses_joined.get(id=course_id)
    except:
        # user is not a student of the course or course does not exist
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {"room": room})
