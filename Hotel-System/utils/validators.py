# utils/validators.py - Validation Functions

from datetime import datetime

def validate_guest_name(name):
    """Validate guest name"""
    if not name or not name.strip():
        return False, "Guest name cannot be empty"
    
    if len(name.strip()) < 2:
        return False, "Guest name must be at least 2 characters"
    
    if len(name.strip()) > 50:
        return False, "Guest name must be less than 50 characters"
    
    return True, ""

def validate_date(date_str):
    """Validate date in YYYY-MM-DD format"""
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return True, date_obj, ""
    except ValueError:
        return False, None, "Invalid date format. Use YYYY-MM-DD"

def validate_room_number(room_number, valid_rooms):
    """Validate room number exists"""
    if room_number in valid_rooms:
        return True, ""
    return False, f"Room {room_number} does not exist"

def validate_contact_info(contact):
    """Validate contact information"""
    if not contact or not contact.strip():
        return False, "Contact information cannot be empty"
    
    # Basic email or phone validation
    if '@' in contact:  # Email
        if len(contact) > 100:
            return False, "Email is too long"
    else:  # Phone
        if not contact.replace(' ', '').replace('-', '').replace('+', '').isdigit():
            return False, "Invalid phone number format"
    
    return True, ""

def validate_special_requests(requests):
    """Validate special requests"""
    if requests and len(requests) > 500:
        return False, "Special requests must be less than 500 characters"
    return True, ""