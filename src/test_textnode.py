import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_one(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)
    
    def test_eq_two(self):
        node1 = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.google.dev")
        self.assertNotEqual(node1, node2)
    def test_eq_three(self):
        node1 = TextNode("This is a text node", TextType.LINK, "https://www.google.dev")
        node2 = TextNode("This is a text node, maybe", TextType.LINK, "https://www.google.dev")
        self.assertNotEqual(node1, node2)
    def test_eq_four(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.google.dev")
        self.assertNotEqual(node1, node2)
    

if __name__ == "__main__":
    unittest.main()