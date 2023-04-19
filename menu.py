from waitlist import Waitlist, Time
class Menu:
    """A class representing the menu for the restaurant reservation program"""

    def __init__(self):
        """Initialize the menu with the waitlist object"""
        self.waitlist = Waitlist()

    def read_time_input(self, message):
        while True:
            time_str = input(message)
            try:
                hour, minute = time_str.split(":")
                time = Time(hour, minute)
                return time
            except:
                print("Invalid input. Please enter time in the format HH:MM.")
                continue

    def run(self):
        """Print the main menu"""
        print("Welcome to the Restaurant Reservation System!")
        print("==============================================")
        print("Please select an option:")
        print("1. Add a customer to the waitlist")
        print("2. Seat the next customer")
        print("3. Change the time of a customer's reservation")
        print("4. Peek at the next customer")
        print("5. Print the reservation list")
        print("6. Quit")
        print("")
        while True:
            
            choice = input("Enter your choice (1-6): ")
            print("*************************************************")
            #Each one of these options should call a method from Waitlist class 
            if choice == "1":
                name = input("Enter customer name: ")
                time = self.read_time_input("Enter the time of the reservation (HH:MM): ")
                
                self.waitlist.add_customer(name, time)

                print(f"\n{name} has been added to the waitlist at {time}\n")

            elif choice == "2":
                """Seat the next customer"""

                customer = self.waitlist.seat_customer()

                if customer is None:
                    print("There is no customer to be seated.")

                (name, time) = customer
                print(f'Seated Customer: {name}, reservation time: {time}\n')


            elif choice == "3":
                """Change the time of a customer's reservation"""

                name = input("Enter the customer's name: ")
                time = self.read_time_input("Enter the new time of the reservation (HH:MM): ")

                try:
                    self.waitlist.change_reservation(name, time)
                    print(f'{name}\'s reservation time has been changed to {time}')
                except ValueError:
                    print(f"Customer named {name} was not found to have a reservation")

            elif choice == "4":
                """Peek at the next customer"""
                customer = self.waitlist.peek()

                if customer is None:
                    print("There are no customers on the waitlist")
                else:
                    (name, time) = customer
                    print(f"The next customer on the waitlist is: {name}, reservation time: {time}")

            elif choice == "5":
                #"""Print the waitlist"""
                self.waitlist.print_reservation_list()
                print()

            elif choice == "6":
                """exit the program at any time"""
                print("Thank you for using the Restaurant Reservation System!")
                break
            else:
                print("Invalid choice. Try again.")
    

s = Menu()
s.run()

