class HtmlNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None , props: dict = None):
        self.tag = tag
        self.props = props if props is not None else None

        if tag is None: #If tag is none, the element is just plain text and cannot have children
            self.value = value
            self.children = None

        elif value is None and children: #if element has no text (value) it will have children
            self.value = None
            self.children = children

        else:
            self.value = value
            self.children = None

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        #return "".join(f'{key} {value}' for key, value in self.props.items())
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
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
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'


    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag, children=children, props=props)


    def to_html(self):
        print(self.children) #DEBUG
        if self.tag is None:
            raise ValueError("ParentNode cannot have None as tag")
        if self.children is None:
            raise ValueError("ParentNode cannot have None as children")
        

        children_str = ""
        #props_str = "" if not self.props else "".join(f'{k}="{v}"' for k, v in self.props.items())
       
        #result_str = f"<{self.tag}{props_str}>"
        for child in self.children:
            children_str += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_str}</{self.tag}>"
        result_str += f"</{self.tag}>"
        return result_str

            