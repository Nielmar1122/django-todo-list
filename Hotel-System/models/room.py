from datetime import datetime, timedelta

class Room:
    """
    Room structure that stores:
    - Room number (string)
    - Room type (Single, Double, Suite, Family)
    - Price per night (float)
    - Is available? (boolean)
    - Booked by (guest name)
    - Check-in date (datetime)
    - Check-out date (datetime)
    - Special requests (string)
    """
    
    ROOM_TYPES = {
        'Single': {'capacity': 1, 'price_multiplier': 1.0},
        'Double': {'capacity': 2, 'price_multiplier': 1.5},
        'Suite': {'capacity': 3, 'price_multiplier': 2.5},
        'Family': {'capacity': 4, 'price_multiplier': 3.0}
    }
    
    def __init__(self, room_number, room_type, base_price=100):
        self.room_number = room_number
        self.room_type = room_type
        self.base_price = base_price
        self.price_per_night = base_price * self.ROOM_TYPES[room_type]['price_multiplier']
        self.capacity = self.ROOM_TYPES[room_type]['capacity']
        self.is_available = True
        self.booked_by = None
        self.check_in_date = None
        self.check_out_date = None
        self.special_requests = None
        self.booking_id = None
    
    def book(self, guest_name, check_in, check_out, special_requests=None):
        """Book the room if available"""
        if not self.is_available:
            return False, "Room is not available"
        
        if check_in >= check_out:
            return False, "Check-out date must be after check-in date"
        
        if check_in < datetime.now():
            return False, "Check-in date must be in the future"
        
        self.is_available = False
        self.booked_by = guest_name
        self.check_in_date = check_in
        self.check_out_date = check_out
        self.special_requests = special_requests
        self.booking_id = f"BKG-{self.room_number}-{datetime.now().strftime('%Y%m%d%H%M')}"
        
        return True, f"Room {self.room_number} booked successfully!"
    
    def cancel_booking(self):
        """Cancel the booking"""
        if self.is_available:
            return False, "Room is not currently booked"
        
        self.is_available = True
        self.booked_by = None
        self.check_in_date = None
        self.check_out_date = None
        self.special_requests = None
        self.booking_id = None
        
        return True, "Booking cancelled successfully!"
    
    def check_out(self):
        """Check out guest"""
        if self.is_available:
            return False, "Room is not currently occupied"
        
        # Calculate total cost
        nights = (self.check_out_date - self.check_in_date).days
        total_cost = nights * self.price_per_night
        
        # Reset room
        guest_name = self.booked_by
        self.is_available = True
        self.booked_by = None
        self.check_in_date = None
        self.check_out_date = None
        self.special_requests = None
        self.booking_id = None
        
        return True, f"{guest_name} checked out. Total cost: ${total_cost:.2f}"
    
    def get_total_cost(self):
        """Calculate total cost of booking"""
        if self.is_available or not self.check_in_date or not self.check_out_date:
            return 0
        
        nights = (self.check_out_date - self.check_in_date).days
        return nights * self.price_per_night
    
    def get_nights(self):
        """Get number of nights booked"""
        if self.is_available or not self.check_in_date or not self.check_out_date:
            return 0
        
        return (self.check_out_date - self.check_in_date).days
    
    def get_booking_info(self):
        """Get complete booking information"""
        if self.is_available:
            return "Room is currently available"
        
        return {
            'booking_id': self.booking_id,
            'guest': self.booked_by,
            'check_in': self.check_in_date.strftime('%Y-%m-%d'),
            'check_out': self.check_out_date.strftime('%Y-%m-%d'),
            'nights': self.get_nights(),
            'total_cost': self.get_total_cost(),
            'special_requests': self.special_requests or 'None'
        }
    
    def __str__(self):
        status = "Available" if self.is_available else f"Booked by {self.booked_by}"
        return f"Room {self.room_number} ({self.room_type}) - ${self.price_per_night}/night - {status}"
    
    def to_dict(self):
        """Convert room to dictionary"""
        return {
            'room_number': self.room_number,
            'room_type': self.room_type,
            'price_per_night': self.price_per_night,
            'capacity': self.capacity,
            'is_available': self.is_available,
            'booked_by': self.booked_by,
            'check_in_date': self.check_in_date,
            'check_out_date': self.check_out_date,
            'booking_id': self.booking_id
        }
