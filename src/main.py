from create_file_system import copy_all_files, delete_all_public_files
from html_generator import generate_page, generate_pages_recursive
from inline_markdown import split_nodes_delimiter, split_nodes_image, text_to_textnodes
from markdown_Blocks import block_to_block_type, markdown_to_blocks
from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
def test():
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


    node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
    new_nodes = split_nodes_image([node])
    print(new_nodes)


    text = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
    
    nodes = text_to_textnodes(text)
    print(nodes)

    md = """
    This is **bolded** paragraph

    
    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
    blocks = markdown_to_blocks(md)
    print(blocks)

    md2 = '''```This is a heahding
        This is line 2
        This is block 3
```'''
    # blocks = markdown_to_blocks(md)
    block_type = block_to_block_type(md2)
    # print(blocks)
    print(block_type)


def main():
    delete_all_public_files()
    copy_all_files()
    generate_pages_recursive('content/', 'template.html', 'public/')
    # generate_page('content/index.md', 'template.html', 'public/')
    # generate_page('content/contact/index.md', 'template.html', 'public/contact/')
    # generate_page('content/blog/glorfindel/index.md', 'template.html', 'public/blog/glorfindel/')
    # generate_page('content/blog/majesty/index.md', 'template.html', 'public/blog/majesty/')
    # generate_page('content/blog/tom/index.md', 'template.html', 'public/blog/tom/')
if __name__ == "__main__":
    main()