#!/usr/bin/python3
from textnode import *

def main():
    newTextNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(repr(newTextNode))

main()