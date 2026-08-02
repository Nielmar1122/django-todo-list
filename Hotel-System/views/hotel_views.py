
def display_rooms(rooms, title="ROOMS", icon="🏨"):
    """Display a list of rooms with formatting"""
    if not rooms:
        print(f"\n❌ No rooms to display.")
        return
    
    print(f"\n{icon} {title}:")
    print("-" * 65)
    print(f"{'Room':^10} | {'Type':^10} | {'Price':^10} | {'Status':^20} | {'Guest':^12}")
    print("-" * 65)
    
    for room in rooms:
        status = "✅ Available" if room.is_available else "🔒 Booked"
        guest = room.booked_by if room.booked_by else "-"
        print(f"{room.room_number:^10} | {room.room_type:^10} | ${room.price_per_night:^9} | {status:^20} | {guest:^12}")
    
    print("-" * 65)

def display_available_rooms(rooms):
    """Display only available rooms"""
    available = [room for room in rooms if room.is_available]
    
    if not available:
        print("\n❌ No rooms available.")
    else:
        display_rooms(available, "AVAILABLE ROOMS", "✅")

def display_booked_rooms(rooms):
    """Display only booked rooms"""
    booked = [room for room in rooms if not room.is_available]
    
    if not booked:
        print("\n✅ No rooms are currently booked.")
    else:
        display_rooms(booked, "BOOKED ROOMS", "🔒")

def display_room_details(room):
    """Display detailed room information"""
    print("\n🔍 ROOM DETAILS:")
    print("=" * 55)
    print(f"Room Number: {room.room_number}")
    print(f"Room Type: {room.room_type}")
    print(f"Capacity: {room.capacity} guests")
    print(f"Price per Night: ${room.price_per_night:.2f}")
    print(f"Status: {'✅ Available' if room.is_available else '🔒 Booked'}")
    
    if not room.is_available:
        print("\n📋 Booking Information:")
        info = room.get_booking_info()
        print(f"  Booking ID: {info['booking_id']}")
        print(f"  Guest: {info['guest']}")
        print(f"  Check-in: {info['check_in']}")
        print(f"  Check-out: {info['check_out']}")
        print(f"  Nights: {info['nights']}")
        print(f"  Total Cost: ${info['total_cost']:.2f}")
        print(f"  Special Requests: {info['special_requests']}")
    
    print("=" * 55)

def display_hotel_stats(rooms):
    """Display hotel statistics"""
    total = len(rooms)
    available = sum(1 for r in rooms if r.is_available)
    booked = total - available
    occupancy = (booked / total * 100) if total > 0 else 0
    
    # Calculate revenue
    total_revenue = sum(r.get_total_cost() for r in rooms if not r.is_available)
    
    # Room type breakdown
    room_types = {}
    for room in rooms:
        if room.room_type not in room_types:
            room_types[room.room_type] = {'total': 0, 'booked': 0}
        room_types[room.room_type]['total'] += 1
        if not room.is_available:
            room_types[room.room_type]['booked'] += 1
    
    print("\n📊 HOTEL STATISTICS:")
    print("=" * 55)
    print(f"Total Rooms: {total}")
    print(f"✅ Available: {available}")
    print(f"🔒 Booked: {booked}")
    print(f"📈 Occupancy Rate: {occupancy:.1f}%")
    print(f"💰 Total Revenue: ${total_revenue:.2f}")
    
    print("\n📋 Room Type Breakdown:")
    print("-" * 55)
    for room_type, data in room_types.items():
        occupancy_rate = (data['booked'] / data['total'] * 100) if data['total'] > 0 else 0
        print(f"{room_type:10} | Total: {data['total']:2} | Booked: {data['booked']:2} | Occupancy: {occupancy_rate:5.1f}%")
    print("=" * 55)

def display_booking_confirmation(room):
    """Display booking confirmation"""
    info = room.get_booking_info()
    print("\n✅ BOOKING CONFIRMATION:")
    print("=" * 55)
    print(f"Booking ID: {info['booking_id']}")
    print(f"Room: {room.room_number} ({room.room_type})")
    print(f"Guest: {info['guest']}")
    print(f"Check-in: {info['check_in']}")
    print(f"Check-out: {info['check_out']}")
    print(f"Nights: {info['nights']}")
    print(f"Price per night: ${room.price_per_night:.2f}")
    print(f"Total Cost: ${info['total_cost']:.2f}")
    if info['special_requests'] != 'None':
        print(f"Special Requests: {info['special_requests']}")
    print("=" * 55)
    print("Thank you for booking with us! 🏨")