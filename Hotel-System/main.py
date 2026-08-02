# main.py - Main Program Entry Point

from data.sample_data import get_sample_rooms
from views.menu import Menu
from views.hotel_views import (
    display_rooms,
    display_available_rooms,
    display_booked_rooms,
    display_room_details,
    display_hotel_stats,
    display_booking_confirmation
)
from controllers.hotel_controller import HotelController
from utils.validators import (
    validate_guest_name,
    validate_date,
    validate_contact_info,
    validate_special_requests
)

def main():
    """Main program flow"""
    
    # Initialize data and controller
    rooms = get_sample_rooms()
    controller = HotelController(rooms)
    
    print("\n🏨 Welcome to the Hotel Booking System!")
    stats = controller.get_hotel_stats()
    print(f"Total Rooms: {stats['total']} | Available: {stats['available']} | Booked: {stats['booked']}")
    
    while True:
        # Display menu
        Menu.display()
        choice = Menu.get_choice()
        
        if choice == "1":  # Show all rooms
            display_rooms(controller.get_all_rooms(), "ALL ROOMS", "🏨")
            
        elif choice == "2":  # Show available rooms
            display_available_rooms(controller.get_rooms())
            
        elif choice == "3":  # Show booked rooms
            display_booked_rooms(controller.get_rooms())
            
        elif choice == "4":  # Book a room
            # Show available rooms
            available_rooms = controller.get_available_rooms()
            if not available_rooms:
                print("\n❌ No rooms available for booking.")
                continue
            
            display_rooms(available_rooms, "AVAILABLE ROOMS", "✅")
            
            # Get room number
            room_number = input("\nEnter room number to book: ").strip()
            room = controller.get_room_by_number(room_number)
            
            if not room:
                print("❌ Room not found.")
                continue
            
            if not room.is_available:
                print("❌ Room is already booked.")
                continue
            
            # Get guest information
            print(f"\n📋 Booking Room {room.room_number} ({room.room_type})")
            print("-" * 55)
            
            guest_name = input("Guest name: ").strip()
            is_valid, error = validate_guest_name(guest_name)
            if not is_valid:
                print(f"❌ {error}")
                continue
            
            contact_info = input("Contact info (phone/email): ").strip()
            is_valid, error = validate_contact_info(contact_info)
            if not is_valid:
                print(f"❌ {error}")
                continue
            
            # Get dates
            check_in = input("Check-in date (YYYY-MM-DD): ").strip()
            is_valid, check_in_date, error = validate_date(check_in)
            if not is_valid:
                print(f"❌ {error}")
                continue
            
            check_out = input("Check-out date (YYYY-MM-DD): ").strip()
            is_valid, check_out_date, error = validate_date(check_out)
            if not is_valid:
                print(f"❌ {error}")
                continue
            
            special_requests = input("Special requests (optional): ").strip()
            if special_requests:
                is_valid, error = validate_special_requests(special_requests)
                if not is_valid:
                    print(f"❌ {error}")
                    continue
            
            # Process booking
            success, message, booked_room = controller.book_room(
                room_number, guest_name, check_in, check_out, contact_info, special_requests
            )
            
            if success:
                display_booking_confirmation(booked_room)
            else:
                print(f"❌ {message}")
            
        elif choice == "5":  # Cancel booking
            booked_rooms = controller.get_booked_rooms()
            if not booked_rooms:
                print("\n✅ No rooms are currently booked.")
                continue
            
            display_rooms(booked_rooms, "BOOKED ROOMS", "🔒")
            
            room_number = input("\nEnter room number to cancel booking: ").strip()
            success, message, room = controller.cancel_booking(room_number)
            print(f"\n{'✅' if success else '❌'} {message}")
            
        elif choice == "6":  # Check out guest
            booked_rooms = controller.get_booked_rooms()
            if not booked_rooms:
                print("\n✅ No guests currently checked in.")
                continue
            
            display_rooms(booked_rooms, "OCCUPIED ROOMS", "🚪")
            
            room_number = input("\nEnter room number to check out: ").strip()
            success, message, room = controller.check_out_guest(room_number)
            print(f"\n{'✅' if success else '❌'} {message}")
            
        elif choice == "7":  # Show room details
            room_number = input("\nEnter room number: ").strip()
            room = controller.get_room_by_number(room_number)
            
            if room:
                display_room_details(room)
            else:
                print("❌ Room not found.")
            
        elif choice == "8":  # Show hotel stats
            display_hotel_stats(controller.get_rooms())
            
        elif choice == "9":  # Exit
            print("\n👋 Thank you for using the Hotel Booking System!")
            stats = controller.get_hotel_stats()
            print(f"Final Status: {stats['available']} rooms available, {stats['booked']} rooms booked")
            print(f"Total Revenue: ${stats['total_revenue']:.2f}")
            break
            
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()