from datetime import datetime

class Reservation:
    """
    Reservation structure that stores:
    - Reservation ID (string)
    - Guest name (string)
    - Contact info (string)
    - Room numbers (list)
    - Check-in date (datetime)
    - Check-out date (datetime)
    - Total guests (int)
    - Total cost (float)
    - Status (Confirmed, Checked-in, Checked-out, Cancelled)
    - Special requests (string)
    """
    
    def __init__(self, guest_name, contact_info, check_in, check_out, total_guests=1):
        self.reservation_id = f"RES-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.guest_name = guest_name
        self.contact_info = contact_info
        self.room_numbers = []
        self.check_in_date = check_in
        self.check_out_date = check_out
        self.total_guests = total_guests
        self.total_cost = 0
        self.status = 'Confirmed'  # Confirmed, Checked-in, Checked-out, Cancelled
        self.special_requests = None
        self.booking_date = datetime.now()
    
    def add_room(self, room):
        """Add a room to the reservation"""
        self.room_numbers.append(room.room_number)
        self.total_cost += room.get_total_cost()
    
    def remove_room(self, room_number):
        """Remove a room from the reservation"""
        if room_number in self.room_numbers:
            self.room_numbers.remove(room_number)
            return True
        return False
    
    def update_status(self, new_status):
        """Update reservation status"""
        valid_statuses = ['Confirmed', 'Checked-in', 'Checked-out', 'Cancelled']
        if new_status in valid_statuses:
            self.status = new_status
            return True
        return False
    
    def get_duration(self):
        """Get number of nights"""
        return (self.check_out_date - self.check_in_date).days
    
    def __str__(self):
        return f"Reservation #{self.reservation_id} - {self.guest_name} - {self.status} - ${self.total_cost:.2f}"