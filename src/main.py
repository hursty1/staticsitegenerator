from create_file_system import copy_all_files, delete_all_public_files
from html_generator import generate_page, generate_pages_recursive
from inline_markdown import split_nodes_delimiter, split_nodes_image, text_to_textnodes
from markdown_Blocks import block_to_block_type, markdown_to_blocks
from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
import sys

def main():
    if len(sys.argv) == 2:
        base_path = sys.argv[1]
    else:
        base_path = '/'
    delete_all_public_files()
    copy_all_files()
    generate_pages_recursive('content/', 'template.html', 'docs/', base_path)

if __name__ == "__main__":
    main()