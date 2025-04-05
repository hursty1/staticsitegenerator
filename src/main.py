from inline_markdown import split_nodes_delimiter
from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
def main():
    val = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(val)
    p = {
                "href": "https://www.google.com",
                "target": "_blank",
            }
    o1 = HTMLNode(tag="tag", value="Value", props=p)
    print(o1.props_to_html())
    print(o1)
    child_node = LeafNode("span", "child")
    child_node2 = LeafNode("p", "child inner inner")
    parent_node = ParentNode("div", [child_node, child_node2])
    print(parent_node.to_html())

    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )

    print(node.to_html())
    print(LeafNode(None, "Normal text").to_html())

    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())


    node = TextNode("This is text with a **code block** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.CODE)
    print(new_nodes)
if __name__ == "__main__":
    main()