# controllers/hotel_controller.py - Business Logic

from datetime import datetime

class HotelController:
    """Controller that handles hotel operations"""
    
    def __init__(self, rooms):
        self.rooms = rooms
    
    def get_all_rooms(self):
        """Return all rooms"""
        return self.rooms
    
    def get_available_rooms(self):
        """Return only available rooms"""
        return [room for room in self.rooms if room.is_available]
    
    def get_booked_rooms(self):
        """Return only booked rooms"""
        return [room for room in self.rooms if not room.is_available]
    
    def get_room_by_number(self, room_number):
        """Get a room by room number"""
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None
    
    def book_room(self, room_number, guest_name, check_in_str, check_out_str, contact_info, special_requests=None):
        """
        Book a room
        Returns: (success, message, room)
        """
        try:
            # Parse dates
            check_in = datetime.strptime(check_in_str, '%Y-%m-%d')
            check_out = datetime.strptime(check_out_str, '%Y-%m-%d')
            
            # Validate dates
            if check_in < datetime.now():
                return False, "Check-in date must be in the future", None
            
            if check_in >= check_out:
                return False, "Check-out date must be after check-in date", None
            
            # Find room
            room = self.get_room_by_number(room_number)
            if not room:
                return False, f"Room {room_number} not found", None
            
            # Book room
            success, message = room.book(guest_name, check_in, check_out, special_requests)
            if success:
                return True, message, room
            else:
                return False, message, None
                
        except ValueError:
            return False, "Invalid date format. Please use YYYY-MM-DD", None
    
    def cancel_booking(self, room_number):
        """
        Cancel a booking
        Returns: (success, message, room)
        """
        room = self.get_room_by_number(room_number)
        if not room:
            return False, f"Room {room_number} not found", None
        
        if room.is_available:
            return False, "Room is not currently booked", None
        
        success, message = room.cancel_booking()
        return success, message, room
    
    def check_out_guest(self, room_number):
        """
        Check out guest
        Returns: (success, message, room)
        """
        room = self.get_room_by_number(room_number)
        if not room:
            return False, f"Room {room_number} not found", None
        
        if room.is_available:
            return False, "Room is not currently occupied", None
        
        success, message = room.check_out()
        return success, message, room
    
    def get_hotel_stats(self):
        """Get hotel statistics"""
        total = len(self.rooms)
        available = len(self.get_available_rooms())
        booked = len(self.get_booked_rooms())
        occupancy = (booked / total * 100) if total > 0 else 0
        
        revenue = sum(room.get_total_cost() for room in self.rooms if not room.is_available)
        
        # Room type breakdown
        room_types = {}
        for room in self.rooms:
            if room.room_type not in room_types:
                room_types[room.room_type] = {'total': 0, 'booked': 0}
            room_types[room.room_type]['total'] += 1
            if not room.is_available:
                room_types[room.room_type]['booked'] += 1
        
        return {
            'total': total,
            'available': available,
            'booked': booked,
            'occupancy_rate': occupancy,
            'total_revenue': revenue,
            'room_types': room_types
        }
    
    def find_rooms_by_type(self, room_type):
        """Find rooms by type"""
        return [room for room in self.rooms if room.room_type.lower() == room_type.lower()]