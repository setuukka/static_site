from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag: str = None, value: str= None, children: list = None, props: dict = None):
        super().__init__(tag, value, children, props)
        if children is not None:
            self.children = None
              


    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have value")
        if self.tag is None:
            return str(self.value)
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            props_str = " ".join(f'{k}="{v}"' for k, v in self.props.items())
            return f'<{self.tag } {props_str}>{self.value}</{self.tag}>'


    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"