import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_no_url(self):
        node = TextNode("Text without url", TextType.ITALIC)
        node2 = TextNode("Text without url", TextType.ITALIC)
        self.assertEqual(node, node2)
       
    def test_different_text(self):
        node = TextNode("Text without url", TextType.BOLD)
        node2 = TextNode("Different Text without url", TextType.BOLD)    
        self.assertNotEqual(node, node2)
    
    def test_with_url(self):
        node = TextNode("Text without url", TextType.BOLD, "www.google.com")
        node2 = TextNode("Text without url", TextType.BOLD, "www.google.com")    
        self.assertEqual(node, node2)        


if __name__ == "__main__":
    unittest.main()