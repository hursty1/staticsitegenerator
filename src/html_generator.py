from markdown_Blocks import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split('\n')
    title = None
    for line in lines:
        if line.startswith('# '):
            title = line.split('# ',1)[1].strip()
    if title is None:
        raise ValueError("h1 Title is missing")
    return title


def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    
    # with open(from_path, 'r') as f:
    #     mk_file = f.read()
    # mk_file = open(from_path, 'r')
    # mk_contents = mk_file.read()
    mk_contents = read_file(from_path)
    template_contents = read_file(template_path)

    html_content = markdown_to_html_node(mk_contents).to_html()
    title = extract_title(mk_contents)

    template_contents_html = template_contents.replace("{{ Title }}", title)
    template_contents_html = template_contents_html.replace("{{ Content }}", html_content)


    dest_dir_path = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, 'w+') as file:
        file.write(template_contents_html)

def read_file(file_path):
    f = open(file_path)
    contents = f.read()
    f.close()
    return contents

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path,item)

        if os.path.isdir(src_path):
            generate_pages_recursive(src_path, template_path, dest_path)
        else:
            _, ext = os.path.splitext(src_path)
            if ext == '.md':
                generate_page(src_path, template_path, dest_path.replace('.md', '.html'))
            else:
                print(f"Skipping Non-markdown file {src_path}")