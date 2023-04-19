import random
import bisect

class Time:
    """A class that represents time in the format HH:MM"""
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False
    
    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour ==  other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"

class Entry:
    """A class that represents a customer in the waitlist"""
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time
    

class Waitlist:
    def __init__(self):
        self._entries = []

    def add_customer(self, item, priority):
        new_entry = Entry(item, priority)

        if not isinstance(priority, Time):
            raise ValueError("Priority must be of class `Time`")

        left = 0
        right = len(self._entries)
        
        while left < right:
            mid = (left+right)//2
            if self._entries[mid] < new_entry:
                right = mid
            else:
                left = mid+1
        self._entries.insert(left, new_entry)

    def peek(self):
        #peek and see the first customer in the waitlist (i.e., the customer with the highest priority).
        # Return a tuple of the extracted item (customer, time). Return None if the heap is empty

        if len(self._entries) > 0:
            return (self._entries[-1].name, self._entries[-1].time)
        else:
            return None

    def seat_customer(self):
        # The program should extract the customer with the highest priority
        # (i.e., the earliest reservation time) from the priority queue.
        # Return a tuple of the extracted item (customer, time)
        
        customer = None

        if len(self._entries) > 0:
            customer = (self._entries[-1].name, self._entries[-1].time)
            self._entries.pop()

        return customer
        

    def print_reservation_list(self):
        #Prints all customers in order of their priority (reservation time).
        #Maintain the heap property

        for entry in reversed(self._entries):
            print(f'The next customer on the waitlist is: {entry.name}, time: {entry.time}')
        
    def change_reservation(self, name, new_priority):
        #Change the reservation time (priority) for the customer with the given name
        
        if not isinstance(new_priority, Time):
            raise ValueError("Priority must be of type `Time`")
        
        entry_index = None

        for index, entry in enumerate(self._entries):
            if entry.name == name:
                entry_index = index
                break

        if entry_index is None:
            raise ValueError("Person not in waitlist")
        self._entries[entry_index].time = new_priority