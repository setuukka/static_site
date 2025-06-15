import unittest

from htmlnode import HTMLnode

class TestHtmlNode(unittest.TestCase):
    def test_create_html_node_no_children_no_props(self):
        node = HTMLnode("<p>", "This is a text in paragraph", None, None)
        self.assertEqual(node.tag, "<p>")
        self.assertEqual(node.value, "This is a text in paragraph")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_create_html_node_no_children(self):
        node = HTMLnode("<a>", "This is a text in paragraph", None, {"href":"https://www.google.com"})
        self.assertEqual(node.tag, "<a>")
        self.assertEqual(node.value, "This is a text in paragraph")
        self.assertIsNone(node.children)
        self.assertEqual(node.props, {"href":"https://www.google.com"})

    def test_props_to_html(self):
        node = HTMLnode("<a>", "This is a text in paragraph", None, {"href":"https://www.google.com", "target":"_blank"})
        props_output = node.props_to_html()
        self.assertEqual(props_output, ' href="https://www.google.com" target="_blank"')



if __name__ == "__main__":
    unittest.main()