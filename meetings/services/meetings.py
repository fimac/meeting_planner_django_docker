from models import Meeting


def add(meeting):
    m = Meeting(
        title=meeting["title"],
        date=meeting["date"],
        start_time=meeting["start_time"],
        duration=meeting["duration"],
        room=meeting["room"],
    )
    m.save()


def all():
    return Meeting.objects.all()
