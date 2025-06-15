class HTMLnode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"


class LeafNode(HTMLnode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag=tag, value=value, children = None, props = props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Value has no value")
        
        if self.tag:
            if not self.props:
                return f'<{self.tag}>{self.value}</{self.tag}>'
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        if not self.tag:
            return self.value
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

        

        
if __name__ == "__main__":
    node = LeafNode("p", "This is a paragraph of text.")
    print(node.tag, node.value, node.children, node.props)
    print(node)
    node.to_html()