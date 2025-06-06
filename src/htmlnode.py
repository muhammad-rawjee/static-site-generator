class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        res = ""
        if self.props:
            for prop in self.props.keys():
                res += f' {prop}="{self.props[prop]}"'
        return res
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"{self.value}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    def to_html(self):
        if not self.tag:
            raise ValueError
        if self.children is None:
            raise ValueError("I am barren, I have no children")
        # Recursive Soln
        else:
            res = ""
            for child in self.children:
                res += child.to_html()
            res = f"<{self.tag}>{res}</{self.tag}>"
            return res
        
# print(LeafNode("p", "This is a paragraph of text.").to_html())
# "<p>This is a paragraph of text.</p>"
# print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html())
# Expect
# "<a href="https://www.google.com">Click me!</a>"

# node = ParentNode(
#     "p",
#     [
#         LeafNode("b", "Bold text"),
#         LeafNode(None, "Normal text"),
#         LeafNode("i", "italic text"),
#         LeafNode(None, "Normal text"),
#     ],
# )

# print(node.to_html())
# # EXPECTED
# # <p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>

