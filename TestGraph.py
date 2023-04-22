from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """
        
              200         40
        A ---------- B -------- C
        |       ____/           |
    200 |   __/ 140             |
        | /                     |
        D ----------------------
                          150
        
        
        """

        vertices = {'A', 'B', 'C', 'D'}
        edges = ('A', 'B', 200), ('B', 'C', 40), ('C', 'D', 150), ('A', 'D', 200), ('B', 'D', 140)

        self.g = Graph(vertices, edges)

    def test_add_vertex(self):
        start_length = len(self.g)

        self.g.add_vertex('E')

        self.assertEqual(len(self.g), start_length + 1)

        


    
class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """ADD DOCSTRING"""

    # TODO: Which alg do you use here, and why?
    # Alg:
    # Why:
    def test_fewest_flights(self):
        """ADD DOCSTRING"""
 

    # TODO: Which alg do you use here, and why?
    # Alg:
    # Why:
    def test_shortest_path(self):
        """ADD DOCSTRING"""

    # TODO: Which alg do you use here, and why?
    # Alg:
    # Why:
    def test_minimum_salt(self):
        """ADD DOCSTRING"""

unittest.main()