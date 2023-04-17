# This file empty on purpose - add the correct classes/methods below

from dataclasses import dataclass

@dataclass
class Entry:
    """Class for keeping track of an item in a priority queue"""
    item: any
    priority: float

    def __lt__(self, other):
        return self.priority < other.priority
    
    def __eq__(self, other):
        return self.priority == other.priority and self.item == other.item

class PQ_UL:
    def __init__(self):
        self._L = []

    def __len__(self):
        return len(self._L)
    
    def insert(self, item, priority):
        new_entry = Entry(item=item, priority=priority)
        
        self._L.append(new_entry)

    def find_min(self):
        self._L.sort(key=lambda x: x.priority, reverse=True)

        return self._L[-1]
    
    def remove_min(self):
        self._L.sort(key=lambda x: x.priority, reverse=True)

        item = self._L[-1]

        del self._L[-1]

        return item
    
class PQ_OL:
    def __init__(self):
        self._L = []

    def __len__(self):
        return len(self._L)
    
    def insert(self, item, priority):
        new_entry = Entry(item=item, priority=priority)
        
        add_index = 0
        for idx, entry in enumerate(self._L):
            if entry.priority < priority:
                add_index = idx
                break

        self._L.insert(add_index, new_entry)

    def find_min(self):
        return self._L[-1]
    
    def remove_min(self):
        item = self._L[-1]

        del self._L[-1]

        return item