"""Class Room representation"""
from Reservation import reservation


class Room:
    """Hotel room representation"""

    def __init__(self, room_number, rsv=None):
        """Initializes a Room with number & price"""
        self.room_number = room_number
        if rsv is not None:
            self.available = False
            self.reserv = rsv
        else:
            self.available = True
            self.reserv = None

    def make_available(self):
        """Make a room available"""
        self.available = True
        self.reserv = None

    def not_available(self):
        """Make a room un available"""
        self.available = False

    def is_available(self):
        """Return status of the room"""
        return self.available

    def to_dict(self):
        """Make dictionary representation"""
        if self.reserv is not None:
            rsv = self.reserv.to_dict()
        else:
            rsv = None
        return {
            'number': self.room_number,
            'available': self.available,
            'reserv': rsv
        }

    @staticmethod
    def from_dict(data):
        """Creates a Room from a dictionary"""
        rm_num = data['number']
        if data['reserv'] is None:
            rm = Room(rm_num)
        else:
            rsv = reservation.Reservation.from_dict(data['reserv'])
            rm = Room(rm_num, rsv)
        return rm
