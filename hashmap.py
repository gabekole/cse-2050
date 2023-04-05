class HashMap():
    def __init__(self, start_bucket_n = 16, load_limit=.75, min_buckets = 8):
        """
        Initialize the hashmap with a number of starting buckets
        """
        
        self._n_buckets = start_bucket_n
        self._len = 0

        self.load_limit = load_limit

        self._min_buckets = min_buckets

        self._buckets = [[] for i in range(self._n_buckets)]

    def _find_bucket_index(self, key):
        bucket_index = hash(key) % self._n_buckets
        
        return bucket_index
        
    def __len__(self):
        return self._len

    def __contains__(self, requested_key):
        """
        Checks whether a key is present in the map
        """

        bucket_index = self._find_bucket_index(requested_key)
        bucket = self._buckets[bucket_index]

        for key, value in bucket:
            if(key == requested_key):
                return True
        return False

    
    def get(self, requested_key):
        """
        Get the value corresponding the the `requested_key`

        Raises a keyerror if the key is not present in the hashmap
        """

        bucket_index = self._find_bucket_index(requested_key)
        bucket = self._buckets[bucket_index]

        for key, value in bucket:
            if(key == requested_key):
                return value
        
        # If we have reached this point, then the key is not present in the hash map
        raise KeyError
    
    def add(self, requested_key, requested_value):
        """
        Add the value of the requested key to the 
        value requested into the hashmap
    
        Will do nothing if already present in hashmap
        """

        if requested_key in self:
            return
        
        # Find index of bucket `item` should go in (self._find_bucket())
        bucket_index = self._find_bucket_index(requested_key)

        # Add item to end of bucket
        self._buckets[bucket_index].append((requested_key, requested_value))

        # update length
        self._len += 1

        # rehash if necessary (items >= 2*buckets)
        if len(self) >= int(self.load_limit*self._n_buckets):
            self._rehash(int(2*self._n_buckets))


    def remove(self, key):
        """Removes item from HashMap. Removing an item not in HashMap should raise a KeyError."""
        # Check if item is in the Hashmap
        # Raise a KeyError if it is not (and include a helpful message)
        if key not in self:
            raise KeyError(f'Attempted to remove key not in map: {key} 😩') # Very helpful 😀

        # Find index of bucket `item` is in (self._find_bucket())
        bucket_index = self._find_bucket_index(key)

        # Get the value
        value = self.get(key)

        # Remove item from bucket
        self._buckets[bucket_index].remove((key, value))

        # update length
        self._len -= 1

        # rehash if necessary (items <= 1/2*buckets, and 1/2*buckets >= min_buckets)
        if len(self) <= int((1/2)*self._n_buckets) and int((1/2)*self._n_buckets) >= self._min_buckets:
            self._rehash(int((1/2)*self._n_buckets))



    def _rehash(self, bucket_num):
        """Rehashes every item from a hash table with n_buckets to one with bucket_num. bucket_num will be either 2*n_buckets or 1/2*n_buckets, depending on whether we are reahshing up or down."""
        # Make a new list of `bucket_num` empty lists
        bucket_list = [[] for i in range(bucket_num)]

        # Using a for loop, iterate over every bucket in self._L
            # using a for loop, iterate over every item in this bucket
                # Find the index of the new bucket for that item
                # add that item to the correct bucket
        self._n_buckets = bucket_num

        for bucket in self._buckets:
            for key, value in bucket:
                bucket_index = self._find_bucket_index(key)
                bucket_list[bucket_index].append((key, value))

        # Update self._L to point to the new list
        self._buckets = bucket_list