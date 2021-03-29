# This is the type
from graphene import (
    ObjectType,
    String,
    Int,
    relay,
)


class Room(ObjectType):
    class Meta:
        interfaces = (relay.Node,)

    name = String(description="Name of meeting room")
    floor_number = String(description="Floor number")
    room_number = String(description="Room number")
