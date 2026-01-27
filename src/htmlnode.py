class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        formatted = ""
        if self.props:
            for k,v in self.props.items():
                formatted += f' {k}="{v}"'
        return formatted
    

    def __repr__(self):
        return f"HTMLNode({self.tag!r}, {self.value!r}, {self.children!r}, {self.props!r})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    

    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode object must have a value")
        if self.tag is None:
            return self.value
   
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        
    def __repr__(self):
        return f"LeafNode({self.tag!r}, {self.value!r}, {self.props!r})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode object must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have a children list")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"