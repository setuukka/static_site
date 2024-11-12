import unittest

from htmlnode import HtmlNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_single_key_value_pair(self):
        obj = LeafNode(props={'name':'Alice'})
        self.assertEqual(obj.props_to_html(), 'name Alice')
    
    def test_string_instead_of_dict(self):
        with self.assertRaises(AttributeError):
            LeafNode(props = "not a dict").props_to_html()

    def test_base_case(self):
        node = LeafNode(tag = "p", value = "This is a paragraph!", props = {'href':'AWESOME'} )
        self.assertEqual(node.to_html(), '<p href="AWESOME">This is a paragraph!</p>')

    def test_values(self):
        node = LeafNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag, "div",)
        self.assertEqual(
            node.value, "I wish I could read",)
        self.assertEqual(
            node.children, None,)
        self.assertEqual(
            node.props, None,)

    def test_repr(self):
        node = LeafNode(
            tag = "p",
            value = "What a strange world",
            props = {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "LeafNode(p, What a strange world, {'class': 'primary'})",
        )

if __name__  == '__main__':
    unittest.main()


