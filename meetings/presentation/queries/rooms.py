from graphene import (
    ObjectType,
    relay,
)
from .room import Room
from meetings.domain.rooms import Rooms


class RoomConnection(relay.Connection):
    class Meta:
        node = Room


class Query(ObjectType):
    rooms = relay.ConnectionField(RoomConnection)

    def resolve_rooms(self, info, **kwargs):
        return Rooms.all()