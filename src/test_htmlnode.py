import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_one(self):
        htmlNode = HTMLNode("li", "some link", None, props={"href": "https://www.google.com","target": "_blank",\
                                                             }\
                            )
        test =  f" href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(htmlNode.props_to_html(), test)
    
    def test_two(self):
        htmlNode = HTMLNode('a', None, None, {"href": "https://www.apple.com"})
        test = f" href=\"https://www.apple.com\""
        self.assertEqual(htmlNode.props_to_html(), test)
    
    def test_three(self):
        htmlNode = HTMLNode('a', None, None, {"href": "https://www.apple.com"})
        test = f"href=\"https://www.apple.com\""
        self.assertNotEqual(htmlNode.props_to_html(), test)