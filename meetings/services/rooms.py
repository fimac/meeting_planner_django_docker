from meetings.models import Room


def add(name, floor_number, room_number):
    r = Room(name=name, floor_number=floor_number, room_number=room_number)
    r.save()


def all():
    return Room.objects.all()