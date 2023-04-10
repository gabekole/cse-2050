class BSTNode:
    def __init__(self, key, left=None, right=None):
        """Construct a node. By default, left and right children are None"""
        self.key = key
        self.left = left
        self.right = right
    
    # classical iteration (correct but slow)
    def __iter__(self):
        """Classical iteration. Creates a new iterator object, which takes O(n)
        to construct the in-order list then returns items one at a time.
        """
        return BSTNode_Iterator(self)

    # generator based iteration (fast)
    def in_order(self):
        """Generator based iteration. We can return items as soon as we find them,
        and the recursive stack we've built stays in memory until the next call
        due to the `yield` keyword.
        """
        if self.left is not None: yield from self.left.in_order()   # recursively go left
        yield self.key                                              # return this key
        if self.right is not None: yield from self.right.in_order() # recursively go right

    def __repr__(self):
        return f"BSTNode(key={self.key})"
  

    def put(self, key):
        """
        Adds a key to the BSTSet
        """
        if key == self.key:
            return
        
        if key < self.key:
            if self.left is None:
                self.left = BSTNode(key, None, None)
            else:
                self.left.put(key)
        else:
            if self.right is None:
                self.right = BSTNode(key, None, None)
            else:
                self.right.put(key)

    def pre_order(self):

        yield self.key

        if self.left is not None: yield from self.left.in_order()   # recursively go left
        if self.right is not None: yield from self.right.in_order() # recursively go right


    def post_order(self):
        if self.left is not None: yield from self.left.in_order()   # recursively go left
        if self.right is not None: yield from self.right.in_order() # recursively go right

        yield self.key


    

# This technique is slow. We have to queue up the ENTIRE tree before we start 
# returning nodes. See above BSTNode.in_order() for an example that yields
# nodes one at a time without queueing up the whole tree.
class BSTNode_Iterator:
    def __init__(self, node):
        self.queue = []
        self.in_order(node) # Queues up the entire tree
        self.counter = 0

    # in_order traversal/queueing
    def in_order(self, node):
        if node.left is not None: self.in_order(node.left)
        self.queue.append(node)
        if node.right is not None: self.in_order(node.right)

    # Update counter, return item, repeat
    def __next__(self):
        if self.counter < len(self.queue):
            self.counter += 1
            return self.queue[self.counter-1].key
        
        raise StopIteration

