class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    

    def add_left(self, value):
        self.left = BETNode(value)

    def add_right(self, value):
        self.left = BETNode(value)

    def evaluate(self):

        def internal_recursive(node)
            if( node.value in CARD_VAL_DICT):
                return node.value

            if (node.value not in OPERATORS):
                raise ValueError("Invalid node value")
            
            operator = node.value
            
            left_value = node.left.evaluate()
            right_value = node.right.evaluate()

            if operator == '+':
                return left_value + right_value
            elif operator == '-':
                return left_value - right_value
            elif operator == '*':
                return left_value*right_value
            elif operator == "/":
                return left_value/right_value

        internal_recursive(self)
            


        
        
    
    def __repr__(): pass


def create_trees(): pass

def find_solutions(): pass