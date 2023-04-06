class HashMap():
    def __init__(self):
        """
        Initialize the hashmap with a number of starting buckets
        """
        
        self._map = dict()

        
    def __len__(self):
        return len(self._map)

    def __contains__(self, requested_key):
        """
        Checks whether a key is present in the map
        """

        return requested_key in self._map

    def items(self):
        """"
        Returns the items of the map
        
        """
        return self._map.items()


    def get(self, requested_key):
        """
        Get the value corresponding the the `requested_key`

        Raises a keyerror if the key is not present in the hashmap
        """

        if requested_key not in self:
            raise KeyError(f"Key not present in hashmap: {requested_key}")
    
        return self._map[requested_key]
    
    def set(self, requested_key, requested_value):
        """
        Add the value of the requested key to the 
        value requested into the hashmap
    
        Will do nothing if already present in hashmap
        """

        self._map[requested_key] = requested_value


    def remove(self, key):
        """Removes item from HashMap. Removing an item not in HashMap should raise a KeyError."""
        # Check if item is in the Hashmap
        # Raise a KeyError if it is not (and include a helpful message)
        if key not in self:
            raise KeyError(f'Attempted to remove key not in map: {key} 😩') # Very helpful 😀

        del self._map[key]