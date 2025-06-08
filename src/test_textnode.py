import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)        

    def test_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, 'https://google.com')
        node2 = TextNode("This is a text node", TextType.BOLD, 'https://google.com')
        self.assertEqual(node, node2)        

    def test_create_text_node(self):
        node = TextNode("hello", TextType.ITALIC, 'https://www.google.com')
        assert node.text == 'hello'
        assert node.text_type ==TextType.ITALIC
        assert node.url == 'https://www.google.com'

    def test_repr_output(self):
        node = TextNode("text", TextType.CODE, None)
        assert repr(node) == "TextNode('text', code, None)"



if __name__ == "__main__":
    unittest.main()
