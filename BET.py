import itertools

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
    

    def add_left(self, node):
        """
        Adds an item to the left of the current node (self)
        uses copying.
        Returns nothing.
        """
        self.left = BETNode(node.value, left=node.left, right=node.right)

    def add_right(self, node):
        """
        Adds an item to the right of the current node (self)
        uses copying.
        Returns nothing.
        """
        self.right = BETNode(node.value, left=node.left, right=node.right)

    def evaluate(self):
        """
        Recusively evaluates to value of the `self` nodes

        Returns NaN, if there is a divide by zero
        Returns Number, otherwise
        """

        if( self.value in BETNode.CARD_VAL_DICT): # base case
            return BETNode.CARD_VAL_DICT[self.value]

        if (self.value not in BETNode.OPERATORS): # This necessitates it is not a Card nor Operator which indicates an error.
            # Not a number and not a operator
            raise ValueError(f'Invalid node value {self.value}')
        
        operator = self.value
        
        left_value = self.left.evaluate()
        right_value = self.right.evaluate()

        # Apply the operator to the value of the left and right sub trees.
        if operator == '+': 
            return left_value + right_value
        if operator == '-':
            return left_value - right_value
        if operator == '*':
            return left_value*right_value
        if operator == "/":
            if right_value == 0:
                # all operations with NaN result in NaN so this will bubble up
                return float('nan') 
            return left_value/right_value
            


    def __repr__(self):
        """"
        Returns a string representation of the tree as a mathmatical expression
        Output uses infix notation
        """
        if( self.value in BETNode.CARD_VAL_DICT):
            return self.value

        if (self.value not in BETNode.OPERATORS):
            # Not a number and not a operator
            raise ValueError(f'Invalid node value {self.value}')
        
        operator = self.value
    
        left_value = repr(self.left)
        right_value = repr(self.right)

        return '('+left_value+operator+right_value+')'


def postfix_to_tree(tree_post_fix_string):
    """"
    Converts a postfix expression string
    into a tree
    """

    stack = [] # Post fix is easily evaluated with a stack.
    for letter in tree_post_fix_string:
        if letter in BETNode.OPERATORS:
            value_two = stack.pop()
            value_one = stack.pop()

            left = value_one
            right = value_two


            node = BETNode(letter, left, right)
            stack.append(node)
        else:
            stack.append(BETNode(letter))

    return stack[0]

def create_trees(cards):
    MAX_TREES = 7680


    valid_shapes = [
        'CCXCCXX',
        'CCXCXCX',
        'CCCXXCX',
        'CCCXCXX',
        'CCCCXXX',
    ]

    values = []

    for character in cards:
        if character in BETNode.CARD_VAL_DICT:
            values.append(character)

    operator_permutations = list(itertools.product(BETNode.OPERATORS, repeat=3))
    value_permutations = list(itertools.permutations(values))

    combined_product = list(itertools.product(operator_permutations, value_permutations))

    tree_list = set()

    for shape in valid_shapes:
        for pair in combined_product:
            operator_order = pair[0]
            value_order = pair[1]
        
            operator_index = 0
            value_index =0

            tree_post_fix_string = ""
            for character in shape:
                if character == 'C':
                    tree_post_fix_string += (value_order[value_index])
                    value_index += 1
                if character == 'X':
                    tree_post_fix_string += (operator_order[operator_index])
                    operator_index += 1

            tree_list.add(postfix_to_tree(tree_post_fix_string))
                        

    return tree_list



def find_solutions(hand):
    if len(hand) != 4:
        raise ValueError(f'Hand must be of length 4, it is of length {len(hand)}')
    for card in hand:
        if card not in BETNode.CARD_VAL_DICT:
            raise ValueError(f'Invalid card in hand {card}')

    trees = create_trees(hand)
    count = 0

    for tree in trees:
        value = tree.evaluate()
        if value == 24:
            count += 1

    return count