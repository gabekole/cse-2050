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
        self.left = BETNode(node.value, left=node.left, right=node.right)

    def add_right(self, node):
        self.right = BETNode(node.value, left=node.left, right=node.right)

    def evaluate(self):

        def internal_recursive(node):
            if( node.value in BETNode.CARD_VAL_DICT):
                return BETNode.CARD_VAL_DICT[node.value]

            if (node.value not in BETNode.OPERATORS):
                # Not a number and not a operator
                raise ValueError(f'Invalid node value {node.value}')
            
            operator = node.value
            
            left_value = internal_recursive(node.left)
            right_value = internal_recursive(node.right)


            if operator == '+':
                return left_value + right_value
            if operator == '-':
                return left_value - right_value
            if operator == '*':
                return left_value*right_value
            if operator == "/":
                if right_value == 0:
                    # all operations with NaN result in Nan so this will bubble up
                    return float('nan') 
                return left_value/right_value


        return internal_recursive(self)
            


    def __repr__(self):
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
    stack = []
    for letter in tree_post_fix_string:
        if letter in BETNode.CARD_VAL_DICT:
            stack.append(BETNode(letter))
        if letter in BETNode.OPERATORS:
            value_two = stack.pop()
            value_one = stack.pop()

            left = value_one
            right = value_two


            node = BETNode(letter, left, right)
            stack.append(node)

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



def find_solutions(): pass