import unittest
import math

from BET import BETNode, create_trees, find_solutions



class TestBETNode(unittest.TestCase):
    def test_repr(self):
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
           
        """
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)
        self.assertEqual(root.evaluate(), -5)

    # TODO: Add test cases below. Repr is provided for you.
    def test_evaluate_tree1(self):
        r"""String representation
               +
              / \
             2   *
                / \
               2   3
           
        """
        root = BETNode('+')
        root.add_left(BETNode('2'))
        root.add_right(BETNode('*'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('3'))
        expected_str = '(2+(2*3))'
        self.assertEqual(repr(root), expected_str)
        self.assertEqual(root.evaluate(), 8)

    def test_evaluate_tree2(self):
        r"""String representation
                 *
              /     \
             +       /
            / \     / \
           5   Q   3   -
                      / \
                     2   2
           
        """
        root = BETNode('*')
        root.add_left(BETNode('+'))
        root.left.add_left(BETNode('5'))
        root.left.add_right(BETNode('Q'))

        root.add_right(BETNode('/'))
        root.right.add_left(BETNode('3'))
        root.right.add_right(BETNode('-'))
        root.right.right.add_right(BETNode('2'))
        root.right.right.add_left(BETNode('2'))
        expected_str = '((5+Q)*(3/(2-2)))'
        self.assertEqual(repr(root), expected_str)

        # Divide by zero results in NaN
        self.assertTrue(math.isnan(root.evaluate()))


class TestCreateTrees(unittest.TestCase):
    def test_hand1(self):
        trees = create_trees("A234")

        self.assertEqual(len(trees), 7680)
        
    def test_hand2(self): pass
        

class TestFindSolutions(unittest.TestCase):
    def test0sols(self): pass

    def test_A23Q(self): pass
        
unittest.main()