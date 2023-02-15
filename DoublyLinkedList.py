# Do not modify this class
class Node:
    'Node object to be used in DoublyLinkedList'
    def __init__(self, item, _next=None, _prev=None):
        'initializes new node objects'
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        'String representation of Node'
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self, items=None):
        'Construct a new DLL object'
        self._head = None
        self._tail = None
        self._len = 0
        self._nodes = dict()    # dictionary of item:node pairs

        # initialize list w/ items if specified
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        'returns number of nodes in DLL'
        return self._len

    # TODO: Modify the 4 methods below to keep `self._nodes` up-to-date
    def add_first(self, item):
        'adds item to front of dll'
        # add new node as head

        node = Node(item, _next=self._head, _prev=None)
        self._nodes[item] = node

        self._head = node
        self._len += 1
        
        # if that was the first node
        if len(self) == 1: self._tail = self._head

        # otherwise, redirect old heads ._tail pointer
        else: self._head._next._prev = self._head

    def add_last(self, item):
        'adds item to end of dll'
        # add new node as head

        node = Node(item, _next=None, _prev=self._tail)
        self._nodes[item] = node

        self._tail = node
        self._len += 1
        
        # if that was the first node
        if len(self) == 1: self._head = self._tail

        # otherwise, redirect old heads ._tail pointer
        else: self._tail._prev._next = self._tail

    def remove_first(self):
        'removes and returns first item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._head.item

        # move up head pointer
        self._head = self._head._next
        self._len -= 1

        # Remove from dictionary
        self._nodes.pop(item)

        # was that the last node?
        if len(self) == 0: self._tail = None

        else: self._head._prev = None

        return item
        
    def remove_last(self):
        'removes and returns last item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._tail.item

        # move up tail pointer
        self._tail = self._tail._prev
        self._len -= 1

        # Remove from dictionary
        self._nodes.pop(item)

        # was that the last node?
        if len(self) == 0: self._head = None

        else: self._tail._next = None

        return item
        
    def __contains__(self, item):
        """
        Checks whether the provided item is present in the list

        Returns true, value
        """

        return item in self._nodes


    def neighbors(self, item):
        """
        Returns the left and right neigbors of the provided value in the list

        Returns tuple: (left item, right item)

        Note: `left item` or `right item` may be None if the item has no node to its left or right

        Note: Raises KeyError when item is not in the list
        """

        node = self._nodes[item]

        return (node._prev.item, node._next.item)


    def remove_node(self, item):
        """
        Remove an item from the list by its value
        
        Note: Throws KeyError when item is not in the list

        Returns nothing.
        """

        self._nodes.pop(item)