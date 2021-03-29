from meetings.services import rooms as Rooms


def add(meeting):
    Rooms.add(meeting)


def all():
    Rooms.all()