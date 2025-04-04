

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        str = ''
        for k,v in enumerate(self.props):
            str = str + f' {v}="{self.props[v]}"'
        return str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("All leaf nodes must have a value")
          
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        if self.tag is None:
            return self.value        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required!")
        if self.children is None:
            raise ValueError("Children is required!")
        inner_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}>{inner_html}</{self.tag}>"
        # return LeafNode(self.tag, inner_html).to_html()
        # return LeafNode(self.tag, self.children[0].to_html()).to_html()

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
