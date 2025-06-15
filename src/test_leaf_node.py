
import unittest

from textnode import TextNode, TextType

from htmlnode import HTMLnode, LeafNode
 

class TestTextNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Hello, world!", {'href':'www.google.com'})
        self.assertEqual(node.to_html(), '<a href="www.google.com">Hello, world!</a>')      

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

        
if __name__ == "__main__":
    unittest.main()
