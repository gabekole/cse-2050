from BSTNode import BSTNode

# Public interface: users only interact with the class BSTMap.
# Methods in BSTSet often call BSTNode methods, which do the heavy lifting.
class BSTSet:
    def __init__(self):
        self._head = None

    # classic iteration (bad)
    def __iter__(self):
        return iter(self._head)

    # generator based iteration (good)
    def in_order(self):
        yield from self._head.in_order()



    def put(self, key):
        return self._head.put(key)

    def pre_order(self):
        return self._head.pre_order()

    def post_order(self):
        return self._head.post_order()