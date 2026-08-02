class Menu:
    """Menu structure and display"""
    
    MENU_OPTIONS = {
        '1': {'label': 'Show all rooms', 'icon': '🏨'},
        '2': {'label': 'Show available rooms', 'icon': '✅'},
        '3': {'label': 'Show booked rooms', 'icon': '🔒'},
        '4': {'label': 'Book a room', 'icon': '📝'},
        '5': {'label': 'Cancel booking', 'icon': '❌'},
        '6': {'label': 'Check out guest', 'icon': '🚪'},
        '7': {'label': 'Show room details', 'icon': '🔍'},
        '8': {'label': 'Show hotel stats', 'icon': '📊'},
        '9': {'label': 'Exit', 'icon': '👋'}
    }
    
    @classmethod
    def display(cls):
        """Display the main menu"""
        print("\n" + "=" * 55)
        print("🏨 HOTEL ROOM BOOKING SYSTEM")
        print("=" * 55)
        
        for key, option in cls.MENU_OPTIONS.items():
            print(f"{key}. {option['icon']} {option['label']}")
        
        print("-" * 55)
    
    @classmethod
    def get_choice(cls):
        """Get user menu choice"""
        return input("Enter your choice (1-9): ").strip()
    
    @classmethod
    def display_header(cls, title, icon="🏨"):
        """Display a section header"""
        print("\n" + "=" * 55)
        print(f"{icon} {title}")
        print("=" * 55)