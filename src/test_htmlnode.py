import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
    
    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Click me!")
        self.assertEqual(node.to_html(), "<h1>Click me!</h1>")
    
    def test_parent_to_html_one(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )