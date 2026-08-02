# data/sample_data.py - Sample Data

from models.room import Room

def get_sample_rooms():
    """Create and return sample room data"""
    rooms = [
        Room("101", "Single", 100),
        Room("102", "Single", 100),
        Room("103", "Double", 150),
        Room("104", "Double", 150),
        Room("105", "Suite", 250),
        Room("106", "Suite", 250),
        Room("201", "Family", 300),
        Room("202", "Family", 300),
        Room("203", "Double", 150),
        Room("204", "Single", 100)
    ]
    
    # Pre-book some rooms for demo
    from datetime import datetime, timedelta
    
    # Book room 101
    check_in = datetime.now() + timedelta(days=1)
    check_out = datetime.now() + timedelta(days=3)
    rooms[0].book("Maria Santos", check_in, check_out, "Extra pillows")
    
    # Book room 103
    check_in = datetime.now() + timedelta(days=2)
    check_out = datetime.now() + timedelta(days=5)
    rooms[2].book("Juan Dela Cruz", check_in, check_out, "King size bed")
    
    # Book room 105
    check_in = datetime.now() + timedelta(days=1)
    check_out = datetime.now() + timedelta(days=2)
    rooms[4].book("Ana Reyes", check_in, check_out)
    
    return rooms